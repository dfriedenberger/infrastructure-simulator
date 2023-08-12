import svgwrite
from datetime import datetime
from math import sin, cos, pi


class HVSignal:
    def __init__(self,signal_type,allowed_commands,zs1,zs2,zs3):
        self.state = {
            "l1" : "off",
            "l2" : "off",
            "l3" : "off",
            "l4" : "off",
            "l5" : "off",
            "l6" : "off",
            "l7" : "off",
            "l8" : "off"
        }
        self.signal_type = signal_type
        self.allowed_commands = allowed_commands
        self.zs1 = zs1
        self.zs2 = zs2
        self.zs3 = zs3

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
        for cmd in self.allowed_commands:
            commands.append({
                "cmd" : cmd,
                "text" : cmd,
                "color" : self._get_color(cmd)
            })
        return commands

    def control(self,cmd):

        if cmd not in self.allowed_commands:
            raise ValueError(f"Command {cmd} is not allowed")

        new_state = {
            "l1" : "off",
            "l2" : "off",
            "l3" : "off",
            "l4" : "off",
            "l5" : "off",
            "l6" : "off",
            "l7" : "off",
            "l8" : "off"
        }

        for part in cmd.split("+"):
            if part == "Hp0":
                new_state["l1"] = "on"
                continue
            if part == "Hp1":
                new_state["l2"] = "on"
                continue
            if part == "Hp2":
                new_state["l2"] = "on"
                new_state["l3"] = "on"
                continue
            if part == "Sh0":
                new_state["l5"] = "on"
                continue
            if part == "Sh1":
                new_state["l6"] = "on"
                continue
            if part == "Zs1":
                new_state["l4"] = "on"
                continue
            if part == "Zs8":
                new_state["l4"] = "blink"
                continue
            if part == "Zs2":
                new_state["l7"] = "on"
                continue
            if part == "Zs3":
                new_state["l8"] = "on"
                continue
            
            raise ValueError(f"Signal aspect {part} is unknown")

        #TODO validate state
        self.state = new_state

        return {"state" : "Ok"}

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

        if self.zs3:
            svg_document.add(svg_document.rect((10, 10), (80, 80),fill=svgwrite.rgb(0, 0, 0, '%')))
            svg_document.add(svg_document.text(self.zs3, insert = (50, 55), fill=self._get_fill(self.state["l8"],fill_yellow), style = "font-size:60px; font-family:Arial; text-anchor: middle;dominant-baseline: middle;"))

        svg_document.add(svg_document.rect((0, 100), (100, 250),fill=svgwrite.rgb(0, 0, 0, '%')))

        if self.zs1 or self.zs2:
            svg_document.add(svg_document.rect((10, 360), (80, 80),fill=svgwrite.rgb(0, 0, 0, '%')))


        if self.signal_type == "Ausfahrsignal":
            svg_document.add(svg_document.circle(center=(25,150),r=15,fill=self._get_fill(self.state["l2"],fill_green)))
            svg_document.add(svg_document.circle(center=(25,200),r=15,fill=self._get_fill(self.state["l1"],fill_red)))
            svg_document.add(svg_document.circle(center=(75,200),r=15,fill=self._get_fill(self.state["l5"],fill_red)))
            svg_document.add(svg_document.circle(center=(75,235),r=10,fill=self._get_fill(self.state["l6"],fill_white)))
            svg_document.add(svg_document.circle(center=(25,265),r=10,fill=self._get_fill(self.state["l6"],fill_white)))
            svg_document.add(svg_document.circle(center=(25,300),r=15,fill=self._get_fill(self.state["l3"],fill_yellow)))

        if self.signal_type == "Hauptsignal":
            svg_document.add(svg_document.circle(center=(25,150),r=15,fill=self._get_fill(self.state["l4"],fill_red)))
            svg_document.add(svg_document.circle(center=(75,150),r=15,fill=self._get_fill(self.state["l2"],fill_green)))
            svg_document.add(svg_document.circle(center=(25,300),r=15,fill=self._get_fill(self.state["l1"],fill_red)))
            svg_document.add(svg_document.circle(center=(75,300),r=15,fill=self._get_fill(self.state["l3"],fill_yellow)))

        if self.signal_type == "Einfahrsignal":
            svg_document.add(svg_document.circle(center=(75,150),r=15,fill=self._get_fill(self.state["l2"],fill_green)))
            svg_document.add(svg_document.circle(center=(25,300),r=15,fill=self._get_fill(self.state["l1"],fill_red)))
            svg_document.add(svg_document.circle(center=(75,300),r=15,fill=self._get_fill(self.state["l3"],fill_yellow)))

        if self.signal_type == "Blocksignal":
            svg_document.add(svg_document.circle(center=(25,300),r=15,fill=self._get_fill(self.state["l1"],fill_red)))
            svg_document.add(svg_document.circle(center=(75,300),r=15,fill=self._get_fill(self.state["l2"],fill_green)))

        if self.zs1:
            svg_document.add(svg_document.circle(center=(50,380),r=10,fill=self._get_fill(self.state["l4"],fill_white)))
            svg_document.add(svg_document.circle(center=(30,420),r=10,fill=self._get_fill(self.state["l4"],fill_white)))
            svg_document.add(svg_document.circle(center=(70,420),r=10,fill=self._get_fill(self.state["l4"],fill_white)))

        if self.zs2:
            svg_document.add(svg_document.text(self.zs2, insert = (50, 405), fill=self._get_fill(self.state["l7"],fill_yellow), style = "font-size:60px; font-family:Arial; text-anchor: middle;dominant-baseline: middle;"))


        return svg_document.tostring()
    

class AusfahrsignalZs1(HVSignal):

    def __init__(self):
        super().__init__("Ausfahrsignal",["Hp0+Sh0" , "Hp0+Sh1" , "Hp0+Zs1" , "Hp0+Zs8", "Zs1" , "Hp1" , "Hp2" ],True,None,None)
        self.control("Hp0+Sh0")

class AusfahrsignalZs2Zs3(HVSignal):

    def __init__(self):
        super().__init__("Ausfahrsignal",["Hp0+Sh0" , "Hp0+Sh1" , "Hp1" , "Hp1+Zs2" , "Hp1+Zs3","Hp1+Zs2+Zs3" , "Hp2" , "Hp2+Zs2" , "Hp2+Zs3", "Hp2+Zs2+Zs3"],False,"Z","6")
        self.control("Hp0+Sh0")

class HauptsignalZs2Zs3(HVSignal):

    def __init__(self):
        super().__init__("Hauptsignal",["Hp0" , "Hp0+Zs1", "Zs1" , "Hp1" , "Hp1+Zs2" , "Hp1+Zs3","Hp1+Zs2+Zs3" , "Hp2" , "Hp2+Zs2" , "Hp2+Zs3", "Hp2+Zs2+Zs3"],False,"Z","6")
        self.control("Hp0")

class EinfahrsignalZs1(HVSignal):

    def __init__(self):
        super().__init__("Einfahrsignal",["Hp0" , "Hp0+Zs1" , "Hp0+Zs8", "Zs1" , "Hp1" , "Hp2" ],True,None,None)
        self.control("Hp0")

class BlocksignalZs1(HVSignal):

    def __init__(self):
        super().__init__("Blocksignal",["Hp0" , "Hp0+Zs1" , "Hp0+Zs8", "Zs1" , "Hp1" ],True,None,None)
        self.control("Hp0")
