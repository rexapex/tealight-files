from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

from math import sin, cos, pi

running = False
car1 = None

def handle_keydown(key):
  global ax, ay

  if key == "left" or key == "right":
    car1.ax = 1
  elif key == "up" or key == "down":
    car1.ay = 1

def start():
  global car1
  
  background("track.png")
  car1 = car()
  car1.init()
  car1.draw()
  
  running = True
  update()
  
def update():
  global running
  
  while running:
    print("running")
    car1.update()
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
    x = 0
    y = 0
    
  def update(self):
    vx = vx + ax
    vy = vy + ay
    
    x = x + vx
    y = y + vy
    
  def draw(self):
    color("red")
    spot(self.x, self.y, 25)
  
  


start()