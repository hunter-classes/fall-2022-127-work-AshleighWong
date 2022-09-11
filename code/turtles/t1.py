import turtle 

def square(t,x,y,w,color,sidelen): 
  #set the turtle, location, width, color, and length of each side) 
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
square(squirt,100,100,5,"red",80)
square(crush,-100,100,10,"blue", 90)
crush.setheading(45)
square(crush,150,30,2,"yellow",60)

#def triangle(t,x,y,w,sidelen):
#bart = turtle.Turtle()
  #triangle(bart,



wn.exitonclick()
wn.mainloop()