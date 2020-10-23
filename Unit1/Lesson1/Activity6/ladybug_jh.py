#   a116_ladybug.py
import turtle

# create ladybug head
ladybug = turtle.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55)
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
x_pos = -20
y_pos = -55
ladybug.pensize(10)

# draw two sets of dots
while num_dots <= 2:
    ladybug.penup()
    ladybug.goto(x_pos, y_pos)
    ladybug.pendown()
    ladybug.circle(3)
    ladybug.penup()
    ladybug.goto(x_pos + 30, y_pos + 20)
    ladybug.pendown()
    ladybug.circle(2)

    # position next dots
    x_pos = y_pos + 25
    x_pos = x_pos + 5
    num_dots += 1

ladybug.hideturtle()

wn = turtle.Screen()
wn.mainloop()
