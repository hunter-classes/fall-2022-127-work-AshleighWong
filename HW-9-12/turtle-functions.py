#def hexagon
import turtle 

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
