import svgwrite
from datetime import datetime

class Signal2000Hz:

    def __init__(self,signal_type,melder = True):
        self.magnet = "on"
        self.signal_type = signal_type
        self.melder = melder

    def get_commands(self):
        return [
            {
                "cmd" : "on",
                "text" : "Sperren",
                "color" : "danger"
            },
            {
                "cmd" : "off",
                "text" : "Freigeben",
                "color" : "warning"
            }
        ]
        
    def control(self,cmd):
        
        if cmd == "on":
            self.magnet = "on"
        elif cmd == "off":
            self.magnet = "off"
        else:
            return {"state" : f"Unknown command {cmd}"}

        return {"state" : "Ok"}
        
    def _get_fill_melder(self):

        # (wirksam blaues Dauerlicht/unwirksam blaues Blinklicht)
        fill_blue = svgwrite.rgb(36, 197, 243)
        fill_white = svgwrite.rgb(100, 100, 100, '%')

        if self.magnet == "on":
            return fill_blue
        if self.magnet == "off":
            now_t = datetime.now()
            if now_t.second % 2 == 0:
                return fill_blue
            else:
                return fill_white
        raise ValueError(f"Unknown state: {self.magnet}")

    def _get_fill_magnet(self):

        fill_red = svgwrite.rgb(100, 0, 0, '%')
        fill_yellow = svgwrite.rgb(100, 100, 0, '%')

        if self.magnet == "on":
            return fill_red
        if self.magnet == "off":
            return fill_yellow

        raise ValueError(f"Unknown state: {self.magnet}")

    def generate_image(self):


        


        svg_document = svgwrite.Drawing(size = ("150px", "170px"))

        if self.melder:
            svg_document.add(svg_document.circle(center=(75,20),r=19,stroke=svgwrite.rgb(0, 0, 0, '%'),stroke_width=2,fill=self._get_fill_melder()))


        #Ne1 / Trapez-Tafel
        if self.signal_type == "Ne1":
            svg_document.add(svg_document.polygon(points=[(40, 45), (110, 45),(140, 115), (10, 115),],stroke=svgwrite.rgb(0, 0, 0, '%'),stroke_width=12,fill=svgwrite.rgb(100, 100, 100, '%')))


        #Ne5 / Halte-Tafel
        if self.signal_type == "Ne5":
            svg_document.add(svg_document.rect((40, 40), (70, 100),stroke=svgwrite.rgb(0, 0, 0, '%'),stroke_width=2,fill=svgwrite.rgb(100, 100, 100, '%')))
            svg_document.add(svg_document.text("H", insert = (75, 95), fill=svgwrite.rgb(0, 0, 0, '%'), style = "font-size:60px; font-family:Arial; text-anchor: middle;dominant-baseline: middle;"))


        # Magnet
        #svg_document.add(svg_document.rect((80, 145), (60, 15),fill=self._get_fill_magnet(),stroke=svgwrite.rgb(0, 0, 0, '%')))
        #svg_document.add(svg_document.text("2000hz", insert = (110, 153), fill=svgwrite.rgb(0, 0, 0, '%'), style = "font-size:8px; font-family:Arial; text-anchor: middle;dominant-baseline: middle;"))

        
        return svg_document.tostring()

class Trapeztafel2000(Signal2000Hz):

    def __init__(self):
        super().__init__("Ne1")

class Haltetafel2000(Signal2000Hz):

    def __init__(self):
        super().__init__("Ne5")
