from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

from math import sin, cos, pi

from github.rexapex.art.prj_car import car

thisCar = None
otherCars = [None, None, None]

def init():
  background("track.png")

def start():
  global thisCar
  
  thisCar = car()

def handle_frame():
  global thisCar, otherCars
  
  thisCar.update()
  thisCar.draw()
  
  for i in range (0, len(cars)):
    cars[i].draw()

def handle_keydown(key):
  if key == "left":
    thisCar.
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power

init()
start()