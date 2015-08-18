from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

def branch(dir):
  turn(dir)
  
  if touch() == 'fruit':
    while touch() == 'fruit':
      move()
  elif left_side() == 'fruit':
    branch(-1)
  elif right_side() == 'fruit':
    branch(1)

def go():
  branch(0)


go()