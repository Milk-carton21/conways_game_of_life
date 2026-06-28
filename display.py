from dataclasses import dataclass
from typing import TypeAlias
import tkinter as tk
import time
from map import *

CELL_SIZE = 5


def create_window(m):
    root = tk.Tk()
    root.title("Conway's Game of Life")

    canvas = tk.Canvas(
        root,
        width=m.width * CELL_SIZE,
        height=m.height * CELL_SIZE,
        bg="white"
    )

    canvas.pack()

    return root, canvas


def render_window(canvas, m) -> None:
    canvas.delete("all")

    for row in range(m.height):
        for col in range(m.width):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            if m.board_state[row][col] == 1:
                color = "black"
            else:
                color = "white"

            canvas.create_rectangle(
                x,
                y,
                x + CELL_SIZE,
                y + CELL_SIZE,
                fill=color,
                outline="gray"
            )


def run_forever_gui(m, next_board_state) -> None:
    root, canvas = create_window(m)

    current = m

    while True:
        render_window(canvas, current)
        root.update()

        current = next_board_state(current)

        time.sleep(0.1)