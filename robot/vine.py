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
  run = True
  while run:
    if left_side():
      run = False
      branch(-1)
    elif right_side():
      run = False
      branch(1)
    else:
      move()

def go():
  
  while True:
    branch(0)


go()