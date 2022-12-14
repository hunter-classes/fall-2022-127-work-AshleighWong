import turtle 

def sample_function():
  print("this is a function")
  print("it can be used multiple times")



wn = turtle.Screen()
crush = turtle.Turtle()

#draw a square
for i in range(4):
  crush.forward(50)
  crush.right(90)

wn.exitonclick()
wn.mainloop()