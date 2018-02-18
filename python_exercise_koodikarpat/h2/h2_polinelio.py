from turtle import *

def piirra_nelio(a, x, y):

    if x >= 0:
        color("blue")
    elif x < 0:
        color("red")
    up()
    setx(x)
    sety(y)
    down()
    begin_fill()
    forward(a)
    right(90)
    forward(a)
    right(90)
    forward(a)
    right(90)
    forward(a)
    right(90)
    end_fill()
    

piirra_nelio(40, -100, 100)
piirra_nelio(60, 100, -100)
piirra_nelio(100, -50, -20)
piirra_nelio(80, 90, 30)
done()
