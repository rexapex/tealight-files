from tealight.art import (color, line, spot, circle, box, image, text, background, rectangle)

from tealight.art import screen_width, screen_height

from math import sin, cos, pi, sqrt

from github.Krimzar.art.racecar import car

car1 = None      #The player using this computer
car2 = None

outerWallX = 5
outerWallY = 5
outerWallWidth = screen_width-10
outerWallHeight = screen_height-10
innerWallX = 120
innerWallY = 250
innerWallWidth = screen_width-240
innerWallHeight = screen_height-500

wPressed = False
aPressed = False
sPressed = False
dPressed = False
upPressed = False
downPressed = False
rightPressed = False
leftPressed = False

#def init():
  #background("track.png")

def start():
  global car1, car2
  
  car1 = car()
  car2 = car()
  
  car1.change_orientation(1)
  car2.change_orientation(1)

def handle_frame():
  global car1, car2, leftPressed, rightPressed, upPressed, downPressed, aPressed, sPressed, dPressed, wPressed
  
  color("white")
  box(0, 0, screen_width, screen_height)
  color("red")
  
  if leftPressed:
    car1.change_orientation(4)
  elif rightPressed:
    car1.change_orientation(-4)
  elif upPressed:
    car1.Acceleration += 0.01
    if car1.Acceleration > 0.05:
      car1.Acceleration = 0.05
  elif downPressed:
    if car1.Acceleration == 0:
      if car1.Acceleration < -0.05:
        car1.Acceleration = -0.05
      else:
        car1.Acceleration -= 0.01
  
  if aPressed:
    car2.change_orientation(4)
  elif dPressed:
    car2.change_orientation(-4)
  elif wPressed:
    car2.Acceleration += 0.01
    if car2.Acceleration > 0.05:
      car2.Acceleration = 0.05
  elif sPressed:
    if car2.Acceleration == 0:
      if car2.Acceleration < -0.05:
        car2.Acceleration = -0.05
      else:
        car2.Acceleration -= 0.01
  
  car1.update_speed()
  car2.update_speed()
  
  testCollisions()
  
  car1.draw_car()
  car2.draw_car()
  
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
  if car1.CoordD["x"] <= outerWallX:
    car1.CoordD["x"] = outerWallX
    car1.Acceleration = 0
    #car1.Speed = -car1.Speed
    car1.change_orientation(90-car.TotalOrientation)
  elif car1.CoordD["x"] >= outerWallWidth:
    car1.CoordD["x"] = outerWallWidth
    car1.Acceleration = 0
   # car1.Speed = -car1.Speed
    car1.change_orientation(180)
  if car1.CoordD["y"] <= outerWallY:
    car1.CoordD["y"] = outerWallY
    car1.Acceleration = 0
   # car1.Speed = -car1.Speed
    car1.change_orientation(180)
  elif car1.CoordD["y"] >= outerWallHeight:
    car1.CoordD["y"] = outerWallHeight
    car1.Acceleration = 0
   # car1.Speed = -car1.Speed
    car1.change_orientation(180)
    
    
    
  if car2.CoordD["x"] <= outerWallX:
    car2.CoordD["x"] = outerWallX
    car2.Acceleration = 0
    #car1.Speed = -car1.Speed
    car2.change_orientation(180)
  elif car2.CoordD["x"] >= outerWallWidth:
    car2.CoordD["x"] = outerWallWidth
    car2.Acceleration = 0
   # car1.Speed = -car1.Speed
    car2.change_orientation(180)
  if car2.CoordD["y"] <= outerWallY:
    car2.CoordD["y"] = outerWallY
    car2.Acceleration = 0
   # car1.Speed = -car1.Speed
    car2.change_orientation(180)
  elif car2.CoordD["y"] >= outerWallHeight:
    car2.CoordD["y"] = outerWallHeight
    car2.Acceleration = 0
   # car1.Speed = -car1.Speed
    car2.change_orientation(180)
    
  #Inner Wall Collision
  #if boxCollision(thisCar.x, thisCar.y, innerWallX, innerWallY, innerWallWidth, innerWallHeight):
  #  print "Collided with centre box"
  
  
#Returns True if point is inside the box
#def boxCollision(x, y, boxX, boxY, boxWidth, boxHeight):
#  if x >= boxX and x <= boxWidth and y >= boxY and y <= boxHeight:
#    return True
#  else:
#    return False

  
#Returns True if point is inside the circle
#def circleCollision():

def handle_keydown(key):
  global car1, car2, leftPressed, rightPressed, upPressed, downPressed, aPressed, sPressed, dPressed, wPressed
  
  if key == "left":
    leftPressed = True
  elif key == "right":
    rightPressed = True
  elif key == "up":
    upPressed = True
  elif key == "down":
    downPressed = True
  elif key == "a":
    aPressed = True
  elif key == "d":
    dPressed = True
  elif key == "w":
    wPressed = True
  elif key == "s":
    sPressed = True
    
def handle_keyup(key):
  global car1, car2, leftPressed, rightPressed, upPressed, downPressed, aPressed, sPressed, dPressed, wPressed
  
  if key == "left":
    leftPressed = False
  elif key == "right":
    rightPressed = False
  elif key == "up":
    upPressed = False
  elif key == "down":
    downPressed = False
  elif key == "a":
    aPressed = False
  elif key == "d":
    dPressed = False
  elif key == "w":
    wPressed = False
  elif key == "s":
    sPressed = False

#init()
start()