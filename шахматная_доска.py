from turtle import *


def chess_board(side):
    x, y = 0, 0
    for i in range(8):

        if i % 2 == 0:

            for j in range(8):

                if j % 2 == 0:
                    penup()
                    goto(x, y)
                    pendown()
                    fillcolor('black')
                    begin_fill()
                    for _ in range(4):
                        forward(side)
                        right(90)
                    end_fill()

                else:
                    penup()
                    goto(x, y)
                    pendown()

                    for _ in range(4):
                        forward(side)
                        right(90)
                y -= side
        else:

            for j in range(5):

                if j % 2 == 0:
                    penup()
                    goto(x, y)
                    pendown()
                    for _ in range(4):
                        forward(side)
                        right(90)

                else:
                    penup()
                    goto(x, y)
                    pendown()
                    fillcolor('black')
                    begin_fill()
                    for _ in range(4):
                        forward(side)
                        right(90)
                    end_fill()

                y -= side

        x += side
        y = 0


def board(side):
    hideturtle()
    chess_board(side)


board(int(input()))