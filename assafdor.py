import turtle
def getpos(x,y):
   print(x, " ", y)
   player.goto(x,y)

screen = turtle.Screen()
player = turtle.Turtle()
player.shape('turtle')
screen.onclick(getpos)

turtle.mainloop()
