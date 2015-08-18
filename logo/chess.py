from tealight.logo import move, turn

def square(side):
  for i in range(0,4):
    move(side)
    turn(90)

def chessboard():
  sqSize = 8
  for i in range(0, 8):
    for j in range(0, 8):
      square(sqSize)
      move(sqSize)
    angle = 90
    if i % 2 == 0:
      angle *= -1
    turn(angle)
    move(sqSize)
    turn(angle)
    

turn(-90)
chessboard()