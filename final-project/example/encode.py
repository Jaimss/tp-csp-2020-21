#   encode.py
#   Note this will not run in the code editor and must be downloaded
import tkinter as tk
import turtle as trtl
from PIL import ImageGrab

message = "changeme" # Change this to encode a different message. Length limit 20 characters.

# get the chraracters as an integer representation
characters_as_ints = []
for cha in message:
  characters_as_ints.append(ord(cha))
print(characters_as_ints)

# get those ints into bits
characters_as_bits = []
for integ in characters_as_ints:
  characters_as_bits.append('{0:08b}'.format(integ))
print(characters_as_bits)

# get those bits as integers again
bits_as_ints = []
for index in range(0,len(characters_as_bits)):
  for bit in characters_as_bits[index]:
    bits_as_ints.append(bit)
print(bits_as_ints)

# create the drawer
screen = trtl.getscreen()
drawer = trtl.Turtle()

# move the ben to different locations and draw the blue square
drawer.penup()
drawer.goto(-200,221)
drawer.shape("square")
drawer.color("blue")

# the message length and draw each part of the message
message_length = len(bits_as_ints)
index = 0
while index < message_length:
  if index % 8 == 0:
    drawer.goto(-200, drawer.ycor()-21)
  if bits_as_ints[index]=='1':
    drawer.stamp()
  drawer.forward(21)
  index = index + 1

# get the screen
screen = trtl.getscreen()
root = trtl.getcanvas().winfo_toplevel()

# create the image of the screen
def create_image(widget):
    x=root.winfo_rootx()
    y=root.winfo_rooty()
    x1=x+widget.window_width()
    y1=y+widget.window_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save("output.gif")
create_image(screen)

# show what is happening
screen.mainloop()
