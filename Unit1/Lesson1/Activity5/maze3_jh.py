import turtle as trtl

# ----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5


# ------ robot commands
def move(times: int = 1):
    i = 0
    while i < times:
        robot.dot(10)
        robot.fd(50)
        i += 1


def turn_left(times: int = 1):
    i = 0
    while i < times:
        robot.speed(0)
        robot.lt(90)
        robot.speed(2)
        i += 1


def turn_right(times: int = 1):
    j = 0
    i = 0
    while j < times:
        while i < 3:
            turn_left()
            i += 1
        j += 1


# ----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

# ----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

wn.bgpic("maze3.png")  # other file names should be maze2.png, maze3.png

move()
turn_right()
move(2)
turn_left()
move(2)
turn_right()
move(2)
turn_left()
move()

wn.mainloop()
