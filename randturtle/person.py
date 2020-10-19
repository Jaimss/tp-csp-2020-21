import turtle as trtl

painter = trtl.Turtle()

def goto_nodraw(p, x, y):
    p.penup()
    p.goto(x, y)
    p.pendown()


goto_nodraw(painter, 0, 0)
painter.pensize(5)
painter.circle(int(input('Head radius')))
# draw thewhole body and legs
painter.goto(0, -50)
painter.goto(15, -60)
painter.goto(-15, -60)
# draw the arms
goto_nodraw(painter, 0, -25)
painter.goto(15, -20)
goto_nodraw(painter, 0, -25)
painter.goto(-15, -20)

sc = trtl.Screen()
sc.mainloop()


