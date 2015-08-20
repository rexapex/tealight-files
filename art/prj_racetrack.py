from tealight.art import (color, line, spot, circle, box, image, text, background, rectangle)

from tealight.art import screen_width, screen_height

from math import sin, cos, pi

from github.rexapex.art.prj_car import car

thisCar = None                  #The player using this computer
otherCars = [None, None, None]  #Other players connected to game

#def init():
  #background("track.png")

def start():
  global thisCar
  
  thisCar = car()

def handle_frame():
  global thisCar, otherCars
  
  thisCar.update()
  thisCar.draw()
  
 # for i in range (0, len(otherCars)):  #Draw connected players cars
 #   otherCars[i].draw()
  
  #Draw the map
  rectangle(5, 5, screen_width-10, screen_height-10)
  box(90, 90, screen_width-180, screen_height-180)

def handle_keydown(key):
  if key == "left":
    thisCar.editOrientation(-1)
  elif key == "right":
    thisCar.editOrientation(1)
  elif key == "up":
    thisCar.editAcceleration(1)
  elif key == "down":
    thisCar.editAcceleration(-1)

#init()
start()