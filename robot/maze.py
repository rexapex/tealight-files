from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def go():
  dir = 0
  
  while left_side() == False:
    move()
  
  
go()