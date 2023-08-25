import os
import json

from .board import Board
class BoardManager():

    def __init__(self):
        self.boards = {}

    def load(self,path):
        for config_file in [f for f in os.listdir(path) if f.endswith('.json')]:
            with open(f"{path}/{config_file}","r",encoding="UTF-8") as f:
                config = json.load(f)
                bid = os.path.splitext(config_file)[0]
                self.boards[bid] = Board(config)

    def add_board(self,board_id,config):
        self.boards[board_id] = Board(config)


    def get_board(self,board_id):

        if board_id not in self.boards:
            raise ValueError(f"Unknown board {board_id}")

        return self.boards[board_id]
