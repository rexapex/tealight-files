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
    if left_side() == False:
      turn(1)
    elif right_side() == True:
      turn(-1)
    move()
go()