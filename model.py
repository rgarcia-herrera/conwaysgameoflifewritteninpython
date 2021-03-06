import networkx as nx
import random


class Cell:

    def __init__(self, universe, active=False):
        self.u = universe
        self.active = active

    def next_state(self):

        # Any live cell with fewer than two live neighbours dies, as
        # if caused by underpopulation.
        if self.active and self.active_neighbors() < 2:
            return False

        # Any live cell with two or three live neighbours lives on to
        # the next generation.
        if self.active and (self.active_neighbors() == 3 or
                            self.active_neighbors() == 2):
            return True

        # Any live cell with more than three live neighbours dies, as
        # if by overpopulation.
        if self.active and self.active_neighbors() > 3:
            return False

        # Any dead cell with exactly three live neighbours becomes a
        # live cell, as if by reproduction.
        if not self.active and self.active_neighbors() == 3:
            return True

    def active_neighbors(self):
        return sum([1 if n.active else 0
                    for n in self.u.g.neighbors(self)])

    def __repr__(self):
        return str(self.active_neighbors())


class Universe:

    def __init__(self, init_grid=None):
        """ init_grid must be a grid of booleans """

        self.height = len(init_grid)
        self.width = len(init_grid[0])

        self.grid = [[Cell(self, c) for c in row]
                     for row in init_grid]

        self.g = nx.Graph()
        self.tangle()

    def tangle(self):
        """ creates edges in network, connects neighbors together """
        for x in range(self.width):
            for y in range(self.height):
                cell = self.grid[y][x]
                # connect to neighborhood
                for i in [x-1, x, x+1 if x+1 < self.width else -1]:
                    for j in [y-1, y, y+1 if y+1 < self.height else -1]:
                        self.g.add_edge(cell, self.grid[j][i])

        # remove self loops from graph
        self.g.remove_edges_from(self.g.selfloop_edges())


def randomized_grid(width, height):
    return [[random.choice([True, False]) for x in range(width)]
            for y in range(height)]
