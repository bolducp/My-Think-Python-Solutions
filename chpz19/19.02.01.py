#Write a program that creates a GUI with a single button. When the button is
#pressed it should create a second button. When that button is pressed, it should
#create a label that says, Nice job

from swampy.Gui import *

g = Gui()
g.title = "Gui"

def make_nicejob_button():
    g.bu(text="I make nicejob label", command=make_nicejob_label)

def make_nicejob_label():
    g.la(text="nice job")

button1 = g.bu(text="first button", command=make_nicejob_button)

g.mainloop()