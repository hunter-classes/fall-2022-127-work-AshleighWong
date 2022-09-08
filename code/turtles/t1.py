import turtle 

def square(t,x,y,w,color,sidelen): 
  #set the location. color, and width 
  t.up()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.down()
  #draw a square
  for i  in range(4):
    t.forward(sidelen)
    t.right(90)


wn = turtle.Screen()
crush = turtle.Turtle()
square(crush,0,0,1,"green", 50 )


squirt = turtle.Turtle()
squirt.up()
squirt.goto(100,100)
squirt.down()
squirt.color("red")
squirt.width(5)
square(squirt)


wn.exitonclick()
wn.mainloop()