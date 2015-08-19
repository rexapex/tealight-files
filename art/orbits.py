from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

x = screen_width / 2
y = screen_height / 2
vx = 0
vy = 0
ax = 0
ay = 0

gravity = 0.2
drag = 0


power = 0.3

explosionX = 0
explosionY = 0
explosionTime = 0

def star(x, y, c, size, spines):
  
  color(c)
  
  angle = 0
  
  for i in range(0, spines):
    x0 = x + (size * cos(angle))
    y0 = y + (size * sin(angle))
    
    line(x, y, x0, y0)
    
    angle = angle + (2 * pi / spines)

def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    ax = -power
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power
  
  if key == "space":
    explosionX = x
    explosionY = y
    explosionTime = 50

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0

def do_explosion():
  global explosionTime, explosionX, explosionY
  
  if explosionTime > 0:
    star(explosionX, explosionY, "orange", 50-explosionTime, 50-explosionTime)
    explosionTime -= 1
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay + gravity
  
  drag = - vy * 0.005
  vy += drag
  
  x = x + vx
  y = y + vy
  
  do_explosion()
  
  color("blue")
  
  spot(x,y,8)
  
  
