import time
from .test_bild import TestBild
from .ampel import Ampel
from .weiche import Weiche
from .hv_signal import Ausfahrtssignal

class Board:

    def __init__(self,config):

        self.infrastructure = {}
        for item in config['items']:
            print(item['id'],item['type'])
            self.infrastructure[item['id']] = self._get_instance(item['type'])

    def _get_instance(self,item_type):

        if item_type == "TestBild": return TestBild()
        if item_type == "Ampel": return Ampel()
        if item_type == "Weiche": return Weiche()
        if item_type == "Ausfahrtssignal": return Ausfahrtssignal()

        raise ValueError(f"Type {item_type} not supported")


    def get_config(self):

        config = {
            "infrastructure" : []
        }

        for id,item in self.infrastructure.items():


            config['infrastructure'].append({
                "id" : id,
                "commands" : item.get_commands()
            })

        return config
    
    def generate(self,refresh,id):

        if id not in self.infrastructure:
            raise ValueError(f"Unknown Infrastructure {id}")

        while True:
            svg_img = self.infrastructure[id].generate_image()
            yield (b'--frame\r\n' b'Content-Type: image/svg+xml\r\n\r\n' +
                bytearray(svg_img,encoding="UTF-8") + b'\r\n')
            time.sleep(refresh)

    def command(self,id,cmd):

        if id not in self.infrastructure:
            raise ValueError(f"Unknown Infrastructure {id}")

        return self.infrastructure[id].control(cmd)
