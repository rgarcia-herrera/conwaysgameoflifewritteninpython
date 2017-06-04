from model import Universe, randomized_grid
from pprint import pprint


w = 25
h = 30
u = Universe(randomized_grid(w, h))

blinker = [[False, False, False, False, False],
           [False, False, True, False, False],
           [False, False, True, False, False],
           [False, False, True, False, False],
           [False, False, False, False, False]]

#u = Universe(blinker)

for t in range(30):
    pprint(u.grid)

    next_grid = [[u.grid[y][x].next_state() for x in range(u.width)]
                 for y in range(u.height)]

    u = Universe(next_grid)
