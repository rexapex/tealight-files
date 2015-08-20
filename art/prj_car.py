from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

from math import sin, cos, pi

class car:
  x = 0
  y = 0
  orientation = 0
  acceleration = 0
  
  power = 0.3
  
  def update(self):
    x = 0
    
  def draw(self):
    line(5, 10, 15, 5)
    line(5, 0, 15, 5)
    
  def editOrientation(dOri):
    orientation = orientation + dOri
    
  def editAcceleration(da):
    acceleration = acceleration + da
    
