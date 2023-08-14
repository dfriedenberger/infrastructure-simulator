import logging
import asyncio

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi import WebSocket

from starlette.responses import StreamingResponse
from pydantic import BaseModel

from hypercorn.config import Config
from hypercorn.asyncio import serve


from infrastructure_simulator.board_manager import BoardManager


board_manager = BoardManager()
board_manager.load("data")


app = FastAPI()


@app.get("/health")
def health():
    return {"Status": "UP"}


class Command(BaseModel):
    id: str
    cmd: str

@app.post("/control/{board_id}")
def control(board_id: str,command : Command):

    return board_manager.get_board(board_id).command(command.id,command.cmd)

@app.get("/config/{board_id}")
def get_config(board_id : str):

    return board_manager.get_board(board_id).get_config()

@app.websocket("/image-stream/{board_id}")
async def get_image_stream(websocket: WebSocket,board_id):

    board = board_manager.get_board(board_id)
    
    await websocket.accept()
    try:
        while True:
            for id in board.ids():
                image = board.get_image(id)
                await websocket.send_text(id+"#"+image)
            await asyncio.sleep(0.1)

    except Exception as e:
        print(e)
    finally:
        websocket.close()

@app.get("/video-feed/{board_id}/{id}")
async def get_video_feed(board_id,id):

    return StreamingResponse(board_manager.get_board(board_id).generate(0.1,id), 
                             media_type="multipart/x-mixed-replace;boundary=frame")

app.mount("/", StaticFiles(directory="htdocs",html = True))


if __name__ == '__main__':
    logging.basicConfig()
    config = Config()
    config.bind = ["0.0.0.0:8080"]
    asyncio.run(serve(app, config))
