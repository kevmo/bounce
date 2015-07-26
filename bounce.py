from Tkinter import *
import random
import time

# configure tk instance, prep canvas, open
tk = Tk()
tk.title("Bounce!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
tk.mainloop()

