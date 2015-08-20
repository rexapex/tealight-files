from tealight.art import (color, line, spot, circle, box, image, text, background, rectangle)

from tealight.art import screen_width, screen_height

from math import sin, cos, pi

from github.rexapex.art.prj_car import car

thisCar = None                  #The player using this computer
otherCars = [None, None, None]  #Other players connected to game

outerWallX = 5
outerWallY = 5
outerWallWidth = screen_width-10
outerWallHeight = screen_height-10
innerWallX = 120
innerWallY = 250
innerWallWidth = screen_width-240
innerWallHeight = screen_height-500

#def init():
  #background("track.png")

def start():
  global thisCar
  
  thisCar = car()

def handle_frame():
  global thisCar, otherCars
  
  thisCar.update()
  
  testCollisions()
  
  thisCar.draw()
  
 # for i in range (0, len(otherCars)):  #Draw connected players cars
 #   otherCars[i].draw()
  
  #Draw the map
  rectangle(outerWallX, outerWallY, outerWallWidth, outerWallHeight)
  #box(innerWallX, innerWallY, innerWallWidth, innerWallHeight)
  
  spot(screen_width/2, innerWallY, innerWallWidth/2)
  spot(screen_width/2, innerWallHeight, innerWallWidth/2)

  
def testCollisions():
  if thisCar.x <= outerWallX:
    thisCar.x = outerWallX
  elif thisCar.x >= outerWallWidth:
    thisCar.x = outerWallWidth
  
  if thisCar.y <= outerWallY:
    thisCar.y = outerWallY
  elif thisCar.y >= outerWallHeight:
    thisCar.y = outerWallHeight


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