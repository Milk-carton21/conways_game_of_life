import unittest
from map import *


class Tests(unittest.TestCase):

    def test_dead_state_zero_size(self):
        m = dead_state(0, 0)

        self.assertEqual(m.width, 0)
        self.assertEqual(m.height, 0)
        self.assertEqual(m.board_state, [])

    def test_check_neighbors_corner_edge(self):
        m = M(2, 2, [[1, 1], [1, 0]])

        self.assertEqual(check_neighbors(m, 0, 0), 2)

    def test_single_live_cell_dies(self):
        m = M(1, 1, [[1]])

        next_m = next_board_state(m)
        self.assertEqual(next_m.board_state, [[0]])

    def test_full_2_by_2_stays_alive(self):
        m = M(2, 2, [[1, 1], [1, 1]])

        next_m = next_board_state(m)
        self.assertEqual(next_m.board_state, [ [1, 1], [1, 1]])
 

if __name__ == "__main__":
    unittest.main()