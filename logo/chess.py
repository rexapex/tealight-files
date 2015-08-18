from tealight.logo import move, turn

def square(side):
  for i in range(0,4):
    move(side)
    turn(90)

def chessboard(edges, size):
  sqSize = 8
  for i in range(0, 8):
    for j in range(0, 8):
      square(sqSize);
      move(sqSize)
    turn(90)
    move(sqSize)
    turn(90)

turn(-90)
chessboard(12,75)