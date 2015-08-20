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
    x = 0
    y = 0
    
  def draw(self):
    line(5, 10, 15, 5)
    line(5, 0, 15, 5)