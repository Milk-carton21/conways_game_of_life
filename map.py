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


def render(m:M)-> M:
    grid = m.board_state
    for row in grid:
        for cell in row:
            if cell ==1:
                print('■', end='')
            else:
                print('□', end='')
        
        print()
            


a_dead = dead_state(2,4)
a_random = random_state(a_dead)
print(render(a_random))
