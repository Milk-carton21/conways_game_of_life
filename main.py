import time
import os
from map import *
from display import run_forever_gui
def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")
24
def load_board_state(filename: str) -> M:
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    board = []

    for line in lines:
        line = line.strip()

        if line != "":
            row = []
            for char in line:
                row.append(int(char))
            board.append(row)

    height = len(board)
    width = len(board[0])

    return M(width, height, board)

choice = input("Choose starting board:\n"
               "1. Random board\n"
               "2. Load board from file\n"
               "Enter 1 or 2: ")

if choice == "1":
    height = int(input("Enter board height: "))
    width = int(input("Enter board width: "))

    initial_state = random_state(dead_state(height, width))

elif choice == "2":
    filename = input("Enter filename (example: toad.txt): ")
    initial_state = load_board_state(filename)

else:
    print("Invalid choice. Using a random 20x40 board.")
    initial_state = random_state(dead_state(20, 40))

run_forever_gui(initial_state, next_board_state)