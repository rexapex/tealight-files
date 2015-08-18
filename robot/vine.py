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
  while True:
    if left_side():
      branch(-1)
    elif right_side():
      branch(1)
    
    move()

def go():
  
  while True:
    branch(0)


go()