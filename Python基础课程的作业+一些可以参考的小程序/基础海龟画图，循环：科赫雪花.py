#kochdrawv1.py

import turtle
def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def main():
    turtle.setup(800,100)
    turtle.penup()
    turtle.goto(-300,-50)
    turtle.pendown()
    turtle.pensize(2)
    level=3
 ####科赫雪花的大小
    koch(500,level)
    turtle.right(120)
    koch(500, level)
    turtle.right(120)
    koch(500, level)
    turtle.hideturtle()
    turtle.done()
main()