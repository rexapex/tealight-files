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
  
  n = 0
  
  while n < 1111:
    if touch() == 'fruit':
      move()
    elif left_side() == 'fruit':
      branch(-1)
    elif right_side() == 'fruit':
      branch(1)
    else
      turn(2)
      while touch() == None:
        move()
        
    n = n + 1

def go():
  branch(0)


go()