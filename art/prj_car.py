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
    self.x += self.acceleration
    
  def draw(self):
    spot(self.x, self.y, 25)
    
  def editOrientation(self, dOri):
    self.orientation = self.orientation + dOri
    
  def editAcceleration(self, da):
    self.acceleration = self.acceleration + da
    
