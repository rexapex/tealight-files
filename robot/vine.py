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
  
  while n < 1111:
    if touch() == 'fruit':
      move()
    if left_side() == 'fruit':
      branch(-1)
    elif right_side() == 'fruit':
      branch(1)
    n = n + 1

def go():
  branch(0)


go()