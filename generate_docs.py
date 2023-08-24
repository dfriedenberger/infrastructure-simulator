import time
import chevron
from  infrastructure_simulator.board import ITEM_CONFIG
from PIL import Image
from cairosvg import svg2png
from io import BytesIO
from freezegun import freeze_time



def make_gif(instance,filename):
    frames = []
    for i in range(0,2000,100):
        sec = int(i/1000)
        ms = i%1000

        with freeze_time(f"2023-08-24 12:00:0{sec}.{ms}"):
            svg_code = instance.generate_image()
        buf = svg2png(bytestring=svg_code)
        img = Image.open(BytesIO(buf))
        frames.append(img)
    frame_one = frames[0]
    frame_one.save(filename, format="GIF", append_images=frames,
               save_all=True, duration=100, loop=0)

context = {
    "examples": []
}


for config in ITEM_CONFIG:
    example = {
        "title" : config["context"],
        "items" : []
    }
    context["examples"].append(example)
    for item in config["items"]:
        instance = item()
        name = item.__name__
        make_gif(instance,f'docs/{name.lower()}.gif')

        example["items"].append({
            "name" : name,
            "image" : f'docs/{name.lower()}.gif',
            "commands" : instance.get_commands()
        })



with open("README.md.mustache",'r',encoding="UTF-8") as f:
    data = f.read()

with open("README.md",'w',encoding="UTF-8") as f:
    f.write(chevron.render(data,context))

