from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def go():
  while True:
    turn(1)
    if left_side:
      move()
      turn(-1)
  
go()