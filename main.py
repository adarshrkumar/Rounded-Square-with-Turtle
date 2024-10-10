"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

def roundArea(turt, s, d): 
  for i in range(d):
    turt.forward(s)
    turt.left(1)

def roundCorner(turt, s): 
  roundArea(turt, s, 90)


# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()

scale = 200

t.speed(10)
t.up()
t.right(90)
t.forward(scale)
t.right(90)
t.forward(scale/2)
t.left(180)
t.down()

for i in range(4):
  t.speed(1)
  t.forward(scale)
  t.speed(320)
  roundCorner(t, scale/100)

t.speed(1)
screen.mainloop()
