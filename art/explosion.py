


class explosion:
  
  def __init__(self):
    self.time = 50
    self.x = 0
    self.y = 0
  
  def set_pos(self, x, y)
    self.x = x
    self.y = y
    
  def update(self):
    
  def draw():
    if explosionTime > 0:
    star(explosionX, explosionY, "orange", 50-explosionTime, 50-explosionTime)
    explosionTime -= 1
    if explosionTime == 0:
      star(explosionX, explosionY, "white", 50-explosionTime, 50-explosionTime)   