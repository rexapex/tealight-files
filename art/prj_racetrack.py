from tealight.art import (color, line, spot, circle, box, image, text, background, rectangle)

from tealight.art import screen_width, screen_height

from math import sin, cos, pi, sqrt

from github.Krimzar.art.racecar import car

car1 = None                  #The player using this computer
car2 = None

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
  global car1, car2
  
  car1 = car()
  car2 = car()

def handle_frame():
  global car1, car2
  
  car1.update_speed()
  
  testCollisions()
  
  car1.draw_car()
  
 # for i in range (0, len(otherCars)):  #Draw connected players cars
 #   otherCars[i].draw()
  
  #Draw the map
  color("green")
  rectangle(outerWallX, outerWallY, outerWallWidth, outerWallHeight)
  #box(innerWallX, innerWallY, innerWallWidth, innerWallHeight)
  #spot(screen_width/2, innerWallY, innerWallWidth/2)
  #spot(screen_width/2, innerWallHeight+innerWallY, innerWallWidth/2)

  
def testCollisions():
  global car1, car2
  
  #Outer Wall Collision
  if car1.CoordCentre["x"] <= outerWallX:
    car1.CoordCentre["x"] = outerWallX
  elif car1.CoordCentre["x"] >= outerWallWidth:
    car1.CoordCentre["x"] = outerWallWidth
  if car1.CoordCentre["y"] <= outerWallY:
    car1.CoordCentre["y"] = outerWallY
  elif car1.CoordCentre["y"] >= outerWallHeight:
    car1.CoordCentre["y"] = outerWallHeight
    
  #Inner Wall Collision
  #if boxCollision(thisCar.x, thisCar.y, innerWallX, innerWallY, innerWallWidth, innerWallHeight):
  #  print "Collided with centre box"
  
  
#Returns True if point is inside the box
def boxCollision(x, y, boxX, boxY, boxWidth, boxHeight):
  if x >= boxX and x <= boxWidth and y >= boxY and y <= boxHeight:
    return True
  else:
    return False

  
#Returns True if point is inside the circle
#def circleCollision():

def handle_keydown(key):
  global car1, car2
  
  if key == "left":
    car1.change_orientation(-5)
  elif key == "right":
    car1.change_orientation(5)
  elif key == "up":
    car1.change_orientation(5)
  elif key == "down":
    car1.change_orientation(-5)

#init()
start()