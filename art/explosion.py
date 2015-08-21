


class explosion:
  
  def __init__(self):
    self.time = 50
    self.x = 0
    self.y = 0
  
  def set_pos(self, x, y):
    self.x = x
    self.y = y
    
  def star(self, x, y, c, size, spines):
    color(c)
    
    angle = 0
    
    for i in range(0, spines):
      x0 = x + (size * cos(angle))
      y0 = y + (size * sin(angle))
      
      line(x, y, x0, y0)
      
      angle = angle + (2 * pi / spines)
    
  def draw(self):
    if self.time > 0:
      self.star(self.x, self.y, "orange", 50-self.time, 50-self.time)
      self.time -= 1
      return False
    if self.time == 0:
      star(self.x, self.y, "white", 50-self.time, 50-self.time)
      return True
      
  