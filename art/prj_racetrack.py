from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

from math import sin, cos, pi

from github.rexapex.art.prj_car import car

def init():
  background("track.png")

def start():
  car1 = car()
  car1.draw()

init()
start()