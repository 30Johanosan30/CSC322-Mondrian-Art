#CSC 322 Mondrian Art Project



#The library tkinter has a wide variety of usage. 
import tkinter as tk
from random import randrange, random

#Window size 
WIDTH = 900
HEIGHT = 600

#These values here alter how many squares appear and how big the segments are. 
SPLIT_LOW = 60
SPLIT_PENALTY = 1.0

#Select a color randomly. Type in a different word to change its color
#Things are chosen in a range of 0 to 1.
#Which ever number is closer to 1, will appear more frequently. 
#(All colors must be given a number between 0 and 1, all the numbers will
# add together to 1.)
#Indigo, purple, white, pink, yellow, red, green, blue, aquamarine, teal,
#skyblue, 
def randomColor():
  rc = random()
  if rc < 0.0833:
    return "red"
  elif rc < 0.1667:
    return "orange"
  elif rc < 0.25:
    return "yellow"
  elif rc < 0.30:
    return "green"
  elif rc < 0.40:
    return "blue"
  elif rc < 0.50:
    return "indigo"
  elif rc < 0.60:
    return "violet"
  else: 
    return "skyblue"

#
# This function will split the region both vertically and horizontally
#
def split_both(x, y, w, h, canvas):
  hsp = randrange(30, 70) / 100
  vsp = randrange(30, 70) / 100
  left_width = round(hsp * w)
  right_width = w - left_width
  top_height = round(vsp * h)
  bottom_height = h - top_height
  mondrian(x, y, left_width, top_height, canvas)
  mondrian(x + left_width, y, right_width, top_height, canvas)
  mondrian(x, y + top_height, left_width, bottom_height, canvas)
  mondrian(x + left_width, y + top_height, right_width, bottom_height, canvas)

#
# Split so that the regions are side by side
#
def split_h(x, y, w, h, canvas):
  hsp = randrange(30, 70) / 100
  left_width = round(hsp * w)
  right_width = w - left_width
  mondrian(x, y, left_width, h, canvas)
  mondrian(x + left_width, y, right_width, h, canvas)

#
# Split so that one region is above the other
#
def split_v(x, y, w, h, canvas):
  vsp = randrange(30, 70) / 100
  top_height = round(vsp * h)
  bottom_height = h - top_height
  mondrian(x, y, w, top_height, canvas)
  mondrian(x, y + top_height, w, bottom_height, canvas)

#
# Use recursion to draw "art" in a Mondrian style
#
def mondrian(x, y, w, h, canvas):
  # Splits based on the size of the region
  if w > WIDTH / 2 and h > HEIGHT / 2:
    split_both(x, y, w, h, canvas)
  elif w > WIDTH / 2:
    split_h(x, y, w, h, canvas)
  elif h > HEIGHT / 2:
    split_v(x, y, w, h, canvas)
  else:
    # Splits based on random chance
    hsplit = randrange(SPLIT_LOW, max(round(SPLIT_PENALTY * w) + 2, \
                       SPLIT_LOW + 2))
    vsplit = randrange(SPLIT_LOW, max(round(SPLIT_PENALTY * h) + 2, \
                       SPLIT_LOW + 2))

    if hsplit < w and vsplit < h:
      split_both(x, y, w, h, canvas)
    elif hsplit < w:
      split_h(x, y, w, h, canvas)
    elif vsplit < h:
      split_v(x, y, w, h, canvas)

    # No split -- this will fill the region with the colors you've chosen 
    else:
      color = randomColor()
      canvas.create_rectangle(x, y, x + w, y + h, \
                              fill=color, outline="black", width=3)

#Main function 
def main():
  # Create a window with a canvas
  master = tk.Tk()
  master.title('Mondrian Art')
  canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT)
  canvas.pack()

  # This allows the art to be drawn 
  mondrian(0, 0, 900, 600, canvas)
  tk.mainloop()

main()
