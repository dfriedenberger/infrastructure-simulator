import svgwrite
from datetime import datetime
from math import sin, cos, pi

class Ausfahrtssignal:

    def __init__(self):
        self.state = {
            "l1" : "off",
            "l2" : "off",
            "l3" : "off",
            "l4" : "off",
            "l5" : "off",
            "l6" : "off"
        }

    def _get_color(self,cmd):
        if cmd.startswith("Hp0"):
            return "danger"
        if cmd.startswith("Hp1"):
            return "success"
        if cmd.startswith("Hp2"):
            return "warning"
        return "primary"
    
    def get_commands(self):

        commands = []
        for cmd in ["Hp0+Sh0" , "Hp0+Sh1" , "Hp0+Zs1" , "Hp0+Zs8", "Zs1" , "Hp1" , "Hp2" ]:
            commands.append({
                "cmd" : cmd,
                "text" : cmd,
                "color" : self._get_color(cmd)
            })
        return commands

    def control(self,cmd):

        #default
        new_state = {
            "l1" : "off",
            "l2" : "off",
            "l3" : "off",
            "l4" : "off",
            "l5" : "off",
            "l6" : "off"
        }

        if cmd == "Hp0+Sh0":
            new_state["l1"] = "on"
            new_state["l5"] = "on"
        if cmd == "Hp0+Sh1":
            new_state["l1"] = "on"
            new_state["l6"] = "on"
        if cmd == "Hp1":
            new_state["l2"] = "on"
        if cmd == "Hp2":
            new_state["l2"] = "on"
            new_state["l3"] = "on"
        if cmd == "Zs1":
            new_state["l4"] = "on"
        if cmd == "Hp0+Zs1":
            new_state["l1"] = "on"
            new_state["l4"] = "on"
        if cmd == "Hp0+Zs8":
            new_state["l1"] = "on"
            new_state["l4"] = "blink"
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
        svg_document = svgwrite.Drawing(size = ("100px", "450px"))

        fill_green = svgwrite.rgb(0, 100, 0, '%')
        fill_red = svgwrite.rgb(100, 0, 0, '%')
        fill_yellow = svgwrite.rgb(100, 100, 0, '%')
        fill_white = svgwrite.rgb(100, 100, 100, '%')


        #svg_document.add(svg_document.rect((10, 10), (80, 80),fill=svgwrite.rgb(0, 0, 0, '%')))
        #svg_document.add(svg_document.text("6", insert = (50, 55), fill=svgwrite.rgb(100, 100, 0, '%'), style = "font-size:60px; font-family:Arial; text-anchor: middle;dominant-baseline: middle;"))

        svg_document.add(svg_document.rect((0, 100), (100, 250),fill=svgwrite.rgb(0, 0, 0, '%')))

        svg_document.add(svg_document.rect((10, 360), (80, 80),fill=svgwrite.rgb(0, 0, 0, '%')))

        # l1 - l6
        svg_document.add(svg_document.circle(center=(25,150),r=15,fill=self._get_fill(self.state["l2"],fill_green)))

        svg_document.add(svg_document.circle(center=(25,200),r=15,fill=self._get_fill(self.state["l1"],fill_red)))
        svg_document.add(svg_document.circle(center=(75,200),r=15,fill=self._get_fill(self.state["l5"],fill_red)))
        
        svg_document.add(svg_document.circle(center=(75,235),r=10,fill=self._get_fill(self.state["l6"],fill_white)))
        svg_document.add(svg_document.circle(center=(25,265),r=10,fill=self._get_fill(self.state["l6"],fill_white)))


        svg_document.add(svg_document.circle(center=(25,300),r=15,fill=self._get_fill(self.state["l3"],fill_yellow)))

        #l4
        
        svg_document.add(svg_document.circle(center=(50,380),r=10,fill=self._get_fill(self.state["l4"],fill_white)))
        svg_document.add(svg_document.circle(center=(30,420),r=10,fill=self._get_fill(self.state["l4"],fill_white)))
        svg_document.add(svg_document.circle(center=(70,420),r=10,fill=self._get_fill(self.state["l4"],fill_white)))




        return svg_document.tostring()
