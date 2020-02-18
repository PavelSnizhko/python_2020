import tkinter as tk
from random import randint

from python_2020.my_balls import tick

WIDTH = 300
HEIGHT = 200


def canvas_click_hendler(event):
    print(event.x, event.y)


def tick():
    global x, y, dx, dy
    x += dx
    y += dy
    print(dx)
    print(dy)
    if x + R > WIDTH or x - R <= 0:
        dx = -dx
        print(dx)
    if y + R > HEIGHT or y - R <= 0:
        dy = -dy
        print(dy)

    canvas.move(ball_id, dx, dy)
    root.after(10, tick)


def main():
    global root, canvas
    global ball_id, x, y, dx, dy, R

    root = tk.Tk()
    root.geometry("800x600")

    canvas = tk.Canvas(root)
    canvas.pack(anchor="nw", fill=tk.BOTH)
    canvas.bind('<Button-1>', canvas_click_hendler)

    R = randint(20, 50)
    x = randint(R, WIDTH - R)
    print(x)

    y = randint(R, HEIGHT - R)
    print(y)
    dx, dy = (+2, +3)
    ball_id = canvas.create_oval(x - R, y - R, x + R, y + R, fill="green")

    tick()
    root.mainloop()


if __name__ == '__main__':
    main()
