from Tkinter import *
import random
import time


tk = Tk()

tk.title("Bounce!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

# game board
canvas = Canvas(tk, width=500, height=400,
                bd=0, highlightthickness=0) # no border
canvas.pack() # size yourself according to previous line
tk.update() # fire ze missile



#models
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        # identifier for this ball
        self.id = canvas.create_oval(10, 10, 25, 25,
                                     fill=color)
        self.canvas.move(self.id, 245, 100)

        # positioning
        starts = range(-3, 4)
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        print "POS:", pos

        if pos[1] < 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <=0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


if __name__ == '__main__':
    ball = Ball(canvas, 'red')
    # tk.mainloop()
    while 1:
        ball.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    pass
