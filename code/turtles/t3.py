import turtle 

wn = turtle.Screen()
crush = turtle.Turtle()

#draw a square
crush.forward(50)
crush.right(90) # turns 90 degrees

crush.forward(50)
crush.right(90)

crush.forward(50)
crush.right(90)

crush.forward(50)
crush.right(90)

#create a second turtle 
#into the variable quirt
#and make aquirt draw a triangle 

squirt = turtle.Screen()
squirt = turtle.Turtle()
#or just squirt =  turtle.Turtle()

squirt.up()
squirt.goto(100,100)
squirt.down()
squirt.color("red") #makes turtle red
squirt.width(5) # makes the line width thicker
for i in range(3):
  squirt.forward(50)
  squirt.right(120)


wn.exitonclick()
wn.mainloop()