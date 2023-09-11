import turtle
#13
#Write a turtle graphics that draws a circle with a radius of 75 px. 
turtle.setup(800,600)
board = turtle.Turtle()
 
board.penup()
board.setpos(0,0)
board.pendown()
board.circle(100)
 
turtle.done()