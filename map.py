from dataclasses import dataclass
from typing import TypeAlias
import random



@dataclass(frozen=True)
class M:
    width: int     
    height: int   
    board_state: list[list[int]]


def dead_state(height: int, width: int) -> M:
    new_state= [[0 for _ in range(width)] for _ in range(height)]
    return M(width, height, new_state)

def random_state(m: M) -> M:
    new_state = [
        [random.randint(0, 1) for _ in range(m.width)]
        for _ in range(m.height)
    ]
    return M(m.width, m.height, new_state)


def render(m:M)->None:
    grid = m.board_state
    for row in grid:
        for cell in row:
            if cell ==1:
                print('■', end='')
            else:
                print('□', end='')
        
        print()
            
def check_neighbors(m: M, row: int, col: int) -> int:
    count = 0

    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):

            if r == row and c == col:
                continue

            # Ignore positions outside the board.
            if 0 <= r < m.height and 0 <= c < m.width:
                if m.board_state[r][c] == 1:
                    count += 1

    return count


def next_board_state(m: M) -> M:
    new_state = []

    for row in range(m.height):
        new_row = []

        for col in range(m.width):
            neighbors = check_neighbors(m, row, col)
            current = m.board_state[row][col]

            if current == 1:
                if neighbors < 2:
                    new_row.append(0)      # Underpopulation
                elif neighbors <= 3:
                    new_row.append(1)      # Survival
                else:
                    new_row.append(0)      # Overpopulation
            else:
                # Dead cell
                if neighbors == 3:
                    new_row.append(1)      # Reproduction
                else:
                    new_row.append(0)

        new_state.append(new_row)

    return M(m.width, m.height, new_state)


a_dead = dead_state(2,4)
a_random = random_state(a_dead)
render(a_random)
