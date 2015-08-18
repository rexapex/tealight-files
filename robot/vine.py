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
      branch(-1)
      run = False
    elif right_side():
      branch(1)
      run = False
    else:
      move()

def go():
  
  while True:
    branch(0)


go()