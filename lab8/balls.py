import pygame
from pygame.draw import *
from tkinter import *

from random import randint
from random import randrange as rnd, choice

import time

root = Tk()

root.geometry('800x600')

canv = Canvas(root, bg='white')

l = Label(root, bg='black', fg='white', width=40)

l.pack()

canv.pack(fill=BOTH, expand=1)

i = 0

balls = []

colors = ['red', 'orange', 'yellow', 'green', 'blue']

a = 600


def new_ball():
    global x, y, r
    x = rnd(100, 700)

    y = rnd(100, 500)

    r = rnd(30, 50)

    vx = rnd(-3, 3)

    vy = rnd(-3, 3)

    id_ = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)

    ball = {

        'id': id_,

        'x': x,

        'y': y,

        'vx': vx,

        'vy': vy

    }

    balls.append(ball)

    root.after(a, new_ball)

    l['text'] = 'Score: ' + str(i)


def click(event):
    global i, a

    for k, b in enumerate(balls):

        if (event.x - b['x']) ** 2 + (event.y - b['y']) ** 2 <= r ** 2:
            i += 1

            canv.delete(b['id'])

            del balls[k]

    print('click')


def motion():
    for b in balls:

        if b['x'] < r or b['x'] > 800 - r:
            b['vx'] = -b['vx']

        if b['y'] < r or b['y'] > 600 - r:
            b['vy'] = -b['vy']

        canv.move(b['id'], b['vx'], b['vy'])

        b['x'] += b['vx']

        b['y'] += b['vy']

    root.after(10, motion)


new_ball()

motion()

canv.bind('<Button-1>', click)

mainloop()

click
click
