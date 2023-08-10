import svgwrite
from datetime import datetime
from math import sin, cos, pi

class Ampel:

    def __init__(self):
        self.state = {
            "red" : "off",
            "yellow" : "blink",
            "green" : "off"
        }

    def get_commands(self):
        return [
            {
                "cmd" : "halt",
                "text" : "Halt",
                "color" : "danger"
            },
            {
                "cmd" : "achtung",
                "text" : "Achtung",
                "color" : "warning"
            },
            {
                "cmd" : "fahrt",
                "text" : "Fahrt",
                "color" : "success"
            },
            {
                "cmd" : "fahrt_erwarten",
                "text" : "Fahrt erwarten",
                "color" : "success"
            }
        ]
    def control(self,cmd):

        #default
        new_state = {
            "red" : "off",
            "yellow" : "off",
            "green" : "off"
        }

        if cmd == "halt":
            new_state["red"] = "on"
        if cmd == "achtung":
            new_state["yellow"] = "on"
        if cmd == "fahrt":
            new_state["green"] = "on"
        if cmd == "fahrt_erwarten":
            new_state["red"] = "on"
            new_state["yellow"] = "on"
        #TODO validate state

        self.state = new_state

        return "Ok"

    def _get_fill(self,state,fill_on):
        fill_off = svgwrite.rgb(20, 20, 20, '%')
        if state == "on":
            return fill_on
        if state == "off":
            return fill_off
        if state == "blink":
            now_t = datetime.now()
            if now_t.second % 2 == 0:
                return fill_on
            else:
                return fill_off

        raise ValueError(f"Unknown state: {state}")

    def generate_image(self):
        svg_document = svgwrite.Drawing(size = ("400px", "400px"))

    	#Activitaetsindikator  
        svg_document.add(svg_document.rect((150, 100), (100, 200),fill=svgwrite.rgb(0, 0, 0, '%')))

        # rot / gelb / grün
        svg_document.add(svg_document.circle(center=(200,150),r=20,fill=self._get_fill(self.state["red"],svgwrite.rgb(100, 0, 0, '%'))))

        svg_document.add(svg_document.circle(center=(200,200),r=20,fill=self._get_fill(self.state["yellow"],svgwrite.rgb(100, 100, 0, '%'))))

        svg_document.add(svg_document.circle(center=(200,250),r=20,fill=self._get_fill(self.state["green"],svgwrite.rgb(0, 100, 0, '%'))))

        return svg_document.tostring()
