from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

from math import sin, cos, pi


running = False

def start():
  background("track.png")
  car1 = car()
  car1.init()
  car1.draw()
  
  running = True
  update()
  
def update():
  global running
  
  while running:
    draw()
  
def draw():
  car1.draw()

class car:
  x = 0
  y = 0
  vx = 0
  vy = 0
  ax = 0
  ay = 0
  
  def init(self):
    print("Car Initialised")
    
  def draw(self):
    color("red")
    spot(self.x, self.y, 50)
  
  


start()