from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

from math import sin, cos, pi

from github.rexapex.art.prj_car import car

cars = [None]

def init():
  background("track.png")

def start():
  car1 = car()
  cars[0] = car1

def handle_frame():
  for i in range (0, len(cars)):
    cars[i].update()
    cars[i].draw()

def handle_keydown(key):
  if key == "left":
    ax = -power
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power  

init()
start()