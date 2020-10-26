import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
line_pos_1 = None


def dragging(x, y):
    """Drag the cursor to draw"""
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)


def clickright(x, y):
    """Clear the screen"""
    t.clear()


def clickleft(x, y):
    """pen up and goto a position"""
    t.penup()
    t.goto(x, y)
    t.pendown()


def middle_click(x, y):
    """Draw a straight line with a middle click"""
    global line_pos_1
    if line_pos_1 is None:
        line_pos_1 = x, y
    else:
        old_x, old_y = line_pos_1
        t.penup()
        t.goto(old_x, old_y)
        t.pendown()
        t.goto(x, y)
        line_pos_1 = None


turtle.listen()

t.ondrag(dragging)
turtle.onscreenclick(clickright, 3)
turtle.onscreenclick(clickleft)
turtle.onscreenclick(middle_click, 2)

screen.mainloop()
