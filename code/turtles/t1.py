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

def position_turtle(t,x,y,w,color,sidelen):

position_turtle(squirt,10,10,5,"red", 20)


def hexagon(t,x,y,w,color,sidelen):
  t.up()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.down()
  for i in range(6):
    t.forward(sidelen)
    t.right(60)

wn = turtle.Screen()
nacho = turtle.Turtle()
hexagon(nacho,50,50,5,"red",80)
cheese = turtle.Turtle()
hexagon(cheese,-100,100,20,"yellow",40)

def ngon(t,numsides,x,y,color,width,sidelen):
  t.up()
  t.goto(x,y)
  t.color(color)
  t.width(width)
  t.down()
  for i in range(numsides):
    t.forward(sidelen)
    t.right(360/numsides)

crazy = turtle.Turtle()
ngon(crazy,50,0,0,"blue",7,10,)
muffin = turtle.Turtle()
ngon(muffin,10,100,100,"purple",3,20)

wn.exitonclick()
wn.mainloop()