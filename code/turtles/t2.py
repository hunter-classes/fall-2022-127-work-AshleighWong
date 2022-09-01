import turtle 

wn = turtle.Screen()
crush = turtle.Turtle()

#draw a square
for i in range(4):
  crush.forward(50)
  crush.right(90)

wn.exitonclick()
wn.mainloop()