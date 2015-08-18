from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def moveBy(spaces):
  for i in range(0, spaces-1):
    move()
  


def go():
  moveBy(4) 
  
  
  
go()