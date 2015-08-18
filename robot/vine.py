from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

def branch():
  while True:
    if touch():
      move()
    if left_side() == 'fruit':
      turn(-1)
    elif right_side() == 'fruit':
      turn(1)




branch()