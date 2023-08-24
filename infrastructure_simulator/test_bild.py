import svgwrite
from datetime import datetime
from math import sin, cos, pi

class TestBild:

    def __init__(self):
        pass
 
    def get_commands(self):
        return []

    def control(self,cmd):
        return {"state" : f"Unknown command {cmd}"}
       
    def generate_image(self):
        svg_document = svgwrite.Drawing(size = ("400px", "400px"))

    	#Activitaetsindikator  
        now_t = datetime.now()

        # Radar
        center = (230, 200)
        radius = 25
        pie_size = 0.1

        start_angle = now_t.microsecond * 2 * pi / 1000000
        end_angle = start_angle + 2 * pi * pie_size

        # Define the start and end points of the arc
        start_point = (center[0] + radius * cos(start_angle), center[1] + radius * sin(start_angle))
        end_point = (center[0] + radius * cos(end_angle), center[1] + radius * sin(end_angle))

        # Draw the arc
        svg_document.add(svg_document.circle(center=center,r=radius,stroke=svgwrite.rgb(100, 100, 100, '%')))
        svg_document.add(svgwrite.path.Path(d=f"M {center[0]},{center[1]} L {start_point[0]},{start_point[1]} A {radius},{radius} 0 0 1 {end_point[0]},{end_point[1]} z", fill="red"))

        # Time
        text = now_t.strftime("%d.%m.%Y %H:%M:%S")
        svg_document.add(svg_document.text(text, insert = (200, 200),  style = "font-size:10px; font-family:Arial; text-anchor: end;dominant-baseline: middle;"))


        return svg_document.tostring()