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
print "BEFO"

print "MAINLOOPIN"
#models
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        pass

if __name__ == '__main__':
    ball = Ball(canvas, 'red')
    tk.mainloop()
    pass


