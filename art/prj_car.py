from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

from math import sin, cos, pi

class car:
  x = 0
  y = 0
  vx = 0
  vy = 0
  ax = 0
  ay = 0
  
  power = 0.3
  
  turn_left = "left"
  turn_right = "right"
  accelerate = "up"
  brake = "down"
  
  def setControls(self, left, right, up, down):
    self.turn_left = left
    self.turn_right = right
    self.accelerate = up
    self.brake = down
  
  def update(self):
    self.vx = self.vx + self.ax
    self.vy = self.vy + self.ay
    
    self.x = self.x + self.vx
    self.y = self.y + self.vy
    
  def draw(self):
    line(5, 10, 15, 5)
    line(5, 0, 15, 5)
    
  def handle_keydown(key):
    global ax, ay
    
    if key == turn_left:
      ax = -power
    elif key == turn_right:
      ax = power
    elif key == accelerate:
      ay = -power
    elif key == brake:
      ay = power  