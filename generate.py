import json
import chevron
from  infrastructure_simulator.board import ITEM_CONFIG
from PIL import Image
from cairosvg import svg2png
from io import BytesIO
from freezegun import freeze_time


def name2id(class_name):
    return class_name.lower().replace("[^a-z0-9]","_")



def make_gif(item_instance,image_filename):
    frames = []
    for i in range(0,2000,100):
        sec = int(i/1000)
        ms = i%1000

        with freeze_time(f"2023-08-24 12:00:0{sec}.{ms}"):
            svg_code = item_instance.generate_image()
        buf = svg2png(bytestring=svg_code)
        img = Image.open(BytesIO(buf))
        frames.append(img)
    frame_one = frames[0]
    frame_one.save(image_filename, format="GIF", append_images=frames,
               save_all=True, duration=100, loop=0)

context = {
    "examples": []
}

hello_world = { "items" : [] }

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
            "details" : f"docs/{name.lower()}.md"
        })

        # Hello world
        hello_world["items"].append({
            "id" : name2id(name),
            "type" : name
        })


        details = "docs/{name.lower()}.md"
        details_context = {
            "name" : name,
            "image" : f'{name.lower()}.gif',
            "commands" : []
        }
        for command in instance.get_commands():
            instance.control(command['cmd'])
            filename = f'{name.lower()}{command["cmd"]}.gif'

            make_gif(instance,f"docs/{filename}")
            details_context["commands"].append({
                "name" : command['text'],
                "cmd" : command['cmd'],
                "item_id" : name2id(name),
                "image" : filename
            })

        with open("templates/Details.md.mustache",'r',encoding="UTF-8") as f:
            data = f.read()

        with open(f"docs/{name.lower()}.md",'w',encoding="UTF-8") as f:
            f.write(chevron.render(data,details_context))

with open("templates/README.md.mustache",'r',encoding="UTF-8") as f:
    data = f.read()

with open("README.md",'w',encoding="UTF-8") as f:
    f.write(chevron.render(data,context))

with open("data/hello-world.json",'w',encoding="UTF-8") as f:
    json.dump(hello_world,f,indent=4)
