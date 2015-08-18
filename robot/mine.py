from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def moveBy(spaces):
  for i in range(0, spaces):
    move()
  


def go():
  moveBy(3) 
  turn(-1)
  while True:
    move()
    
  
  
go()