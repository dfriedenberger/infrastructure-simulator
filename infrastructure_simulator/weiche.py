import svgwrite
from datetime import datetime

class Weiche:

    def __init__(self):
        self.state = {
            "l1" : "off",
            "l2" : "off",
            "l3" : "off"
        }
        self.stellung = "Wn1"
        self.new_stellung = "Wn1"
        self.update = datetime(2020, 1, 1)
        self.umlaufzeit = 10

    def get_commands(self):
        return [
            {
                "cmd" : "Wn1",
                "text" : "Wn1",
                "color" : "primary"
            },
            {
                "cmd" : "Wn2",
                "text" : "Wn2",
                "color" : "primary"
            }
        ]
        
    def control(self,cmd):
        
        now_t = datetime.now()


        #lock
        if (now_t - self.update).total_seconds() <= self.umlaufzeit:
            return "No possible at the moment"

        if self.stellung == cmd:
            return {"state" : f"point yet in state {cmd}"}


        if cmd == "Wn1" or cmd == "Wn2":
            self.new_stellung = cmd
            self.update = now_t
            return {"state" : "Ok"}

        
        return {"state" : f"Unknown command {cmd}"}

    def _update_state(self):
        now_t = datetime.now()

        new_state = {
            "l1" : "off",
            "l2" : "off",
            "l3" : "off"
        }

        if self.stellung != self.new_stellung:
            if (now_t - self.update).total_seconds() > self.umlaufzeit:
                self.stellung = self.new_stellung
            else:
                new_state["l2"] = "blink"

        if self.stellung == self.new_stellung:
            if self.stellung == "Wn1":
                new_state["l1"] = "on"
                new_state["l2"] = "on"
            if self.stellung == "Wn2":
                new_state["l3"] = "on"
                new_state["l2"] = "on"
      
        self.state = new_state

    def _get_fill(self,state):

        fill_off = svgwrite.rgb(20, 20, 20, '%')
        fill_on = svgwrite.rgb(100, 100, 100, '%')
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

        self._update_state()


        svg_document = svgwrite.Drawing(size = ("150px", "150px"))

        svg_document.add(svg_document.rect((0, 0), (150, 150),fill=svgwrite.rgb(0, 0, 0, '%')))

        # rot / gelb / grün
        svg_document.add(svg_document.circle(center=(50,50),r=20,fill=self._get_fill(self.state["l1"])))

        svg_document.add(svg_document.circle(center=(50,100),r=20,fill=self._get_fill(self.state["l2"])))

        svg_document.add(svg_document.circle(center=(100,100),r=20,fill=self._get_fill(self.state["l3"])))

        return svg_document.tostring()
