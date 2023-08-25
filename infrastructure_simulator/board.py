import asyncio
from .test_bild import TestBild
from .ampel import Ampel
from .weiche import Weiche
from .hv_signal import AusfahrsignalZs1 , AusfahrsignalZs2Zs3, HauptsignalZs2Zs3, EinfahrsignalZs1, BlocksignalZs1
from .signal_2000_hz import Haltetafel2000, Trapeztafel2000


ITEM_CONFIG = [
    {
        "context" : "Railway",
        "items" : [ Weiche , AusfahrsignalZs1, AusfahrsignalZs2Zs3 , HauptsignalZs2Zs3 , EinfahrsignalZs1 , BlocksignalZs1 , Trapeztafel2000, Haltetafel2000]
    },
    {
        "context" : "Allgemein",
        "items" : [ Ampel, TestBild ]
    }
]
class NamedInstance:
    def __init__(self,name,instance):
        self.name = name
        self.instance = instance

class Board:

    def __init__(self,config):
        self.item_class_map = {}
        for c in ITEM_CONFIG:
            for item_class in c["items"]:
                self.item_class_map[item_class.__name__] = item_class

        self.infrastructure = {}
        for item in config['items']:
            print(item['id'],item['name'],item['type'])
            self.infrastructure[item['id']] = NamedInstance(item['name'],self._get_instance(item['type']))

        

    def _get_instance(self,item_type):

        if item_type not in self.item_class_map:
            raise ValueError(f"Type {item_type} not supported")

        return self.item_class_map[item_type]()


    def get_config(self):

        config = {
            "infrastructure" : []
        }

        for id,item in self.infrastructure.items():


            config['infrastructure'].append({
                "id" : id,
                "name" : item.name,
                "commands" : item.instance.get_commands()
            })

        return config
    
    def ids(self):
        return list(self.infrastructure.keys())

    def get_image(self,id):
        if id not in self.infrastructure:
            raise ValueError(f"Unknown Infrastructure {id}")

        return self.infrastructure[id].instance.generate_image()


    async def generate(self,refresh,id):

        if id not in self.infrastructure:
            raise ValueError(f"Unknown Infrastructure {id}")

        while True:
            svg_img = self.infrastructure[id].instance.generate_image()
            yield (b'--frame\r\n' b'Content-Type: image/svg+xml\r\n\r\n' +
                bytearray(svg_img,encoding="UTF-8") + b'\r\n')
            await asyncio.sleep(0.1)

    def command(self,id,cmd):

        if id not in self.infrastructure:
            raise ValueError(f"Unknown Infrastructure {id}")

        return self.infrastructure[id].instance.control(cmd)
