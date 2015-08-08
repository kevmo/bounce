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
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
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

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)

        # pos = [x1, y1, x2, y2]
        if pos[2] > paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        print("POS:", pos)

        if pos[1] < 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <=0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:
    def __init__(self, canvas, color):
        # Set up a Canvas
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        # Position properties
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        # Event handlers
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)


    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] > self.canvas_width:
            self.x = 0


if __name__ == '__main__':
    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, paddle, 'red')

    # tk.mainloop()
    while 1:
        if ball.hit_bottom == False:
            ball.draw()
            paddle.draw()

        ball.draw()
        paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.02)
    pass
