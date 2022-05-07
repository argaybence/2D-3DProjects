import time
from tkinter import Tk, Canvas


def quadratic_equation(b, c):  # index stands for x1, or x2
    #  (a) always equal to 1, because of (x - 700)^2 is x^2(1)
    a = 1
    d = (((b * 2) ** 2) - (4 * a * c)) ** (1 / 2)

    return b - int(abs((d / 2))), b + int(abs((d / 2)))


def circle_equation(mid_x, mid_y, y, r):
    #  (x - 700)^2 + (y - 440)^2 = r^2

    z = ((y - mid_y) ** 2) - (r ** 2)
    c = (mid_x ** 2) + z

    return quadratic_equation(int(mid_x), c)


def draw_circle(master, mid_x, mid_y, r, color, height=1, width=1, second=0.001):
    x = {}

    for y_1 in range(mid_y - r, mid_y + (r + 1)):
        x[y_1] = circle_equation(mid_x, mid_y, y_1, r)
        time.sleep(second)
        Canvas(master, width=width, height=height, bg=color, highlightbackground=color).place(x=int(x[y_1][0]), y=y_1)
        master.update()

    for y_2 in reversed(range(mid_y - r, mid_y + (r + 1))):
        x2 = x[y_2][1]
        time.sleep(second)
        Canvas(master, width=width, height=height, bg=color, highlightbackground=color).place(x=x2, y=y_2)
        master.update()


def spiral(master):
    r = 10

    for i in range(0, 500, 20):
        r += 5
        draw_circle(master, 700 + i, 440, r, "blue", second=0)


def circle(master):
    draw_circle(master, 700, 440, 400, "white", second=0, width=1, height=1)


def main():
    win = Tk()
    win.geometry("1400x880")
    win.configure(bg="black")

    big_circle(win)

    win.mainloop()


if __name__ == '__main__':
    main()
