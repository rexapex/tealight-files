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
    elif right_side():
      branch(1)
    else:
      move()

def go():
  branch(0)


go()