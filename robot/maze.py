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
    if left_side() == False || right_side() == False:
      turn(1)
    move()
go()