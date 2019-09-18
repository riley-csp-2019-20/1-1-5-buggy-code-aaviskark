#   a115_buggy_image.py
import turtle as trtl
#create spider body
drawer = trtl.Turtle()
drawer.pensize(40)
drawer.circle(20)
#establish variables for each body part
legs = 4
length = 70
angle = 120 / legs
drawer.pensize(5)
#draw the body parts of the spider
loop = 0
while (loop < legs):
  drawer.goto(0,20)
  drawer.setheading(angle*loop+90)
  drawer.forward(length)
  loop = loop + 1
loop=0
while (loop < legs):
  drawer.goto(0,20)
  drawer.setheading(angle*loop-60)
  drawer.forward(length)
  loop = loop + 1
eye= 0
drawer.pencolor("green")
drawer.penup()
drawer.goto(-10,20)
drawer.pendown()
drawer.circle(10)
drawer.hideturtle()
drawer.penup()
drawer.goto(10,0)
drawer.pendown()
drawer.circle(10)

wn = trtl.Screen()
wn.mainloop()
