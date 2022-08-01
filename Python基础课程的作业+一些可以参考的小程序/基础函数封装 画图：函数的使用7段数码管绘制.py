import time
import turtle

def drawgap():
    turtle.penup()
    turtle.fd(5)


def drawline(draw):
    drawgap()
    turtle.pendown()  if draw else turtle.penup()  #绘制单段数码管
    turtle.fd(40)
    drawgap()
    turtle.right(90)


def drawdigit(digit):    #根据digit 绘制
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawdate(date):
    for i in date:
        drawdigit(eval(i))


def drawdate(date):
    turtle.pencolor("purple")
    for i in date:
        if i=="-":
            turtle.write("年",font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i=="=":
            turtle.write("月",font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i=="+":
            turtle.write("日",font=("Arial",18,"normal"))

        else:
            drawdigit(eval(i))



def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawdate(time.strftime('%Y-%m=%d+',time.gmtime()))
   # drawdate('114-5=14+')
    turtle.hideturtle()
    turtle.done()
main()