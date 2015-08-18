from tealight.logo import move, turn

def square(side):
  for i in range(0,4):
    move(side)
    turn(90)

def chessboard(edges, size):
  for i in range(0, 8):
    for j in range(0, 8):
      square(5);
      move(5)
  turn(angle)

turn(-90)
chessboard(12,75)