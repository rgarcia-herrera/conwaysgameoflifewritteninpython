import networkx as nx
import random


class Cell:

    def __init__(self, universe, active=False):
        self.u = universe
        self.active = active

    def next_state(self):

        # death by isolation
        if self.active_neighbors() <= 2:
            return False

        # keep on truckin'
        if self.active and self.active_neighbors() == 2 \
           or self.active_neighbors() == 3:
            return True

        # death by crowding
        if self.active and self.active_neighbors() > 3:
            return False

        # be born!
        if not self.active and self.active_neighbors() == 3:
            return True

    def active_neighbors(self):
        return sum([1 if n.active else 0 for n in self.u.g.neighbors(self)])

    def __repr__(self):
        return 'x' if self.active else ' '

from pprint import pprint

class Universe:

    def __init__(self, init_grid=None):
        """ mask can be a grid of booleans """

        self.height = len(init_grid)
        self.width = len(init_grid[0])
#        print "u%sx%s" % (self.width, self.height)

#        pprint(init_grid)
        self.grid = [[Cell(self, c) for c in row]
                     for row in init_grid]

        self.g = nx.Graph()
        self.tangle()

    def tangle(self):
        """ creates edges in network, connects neighbors together """
        for x in range(self.width):
#            print "X=", x
            for y in range(self.height):
#                print "Y=", y
                cell = self.grid[y][x]
                # connect to neighborhood
                for i in [x-1, x, x+1 if x+1 < self.width else -1]:
                    for j in [y-1, y, y+1 if y+1 < self.height else -1]:
#                        print j,i
#                        print self.grid[j][i].active
                        self.g.add_edge(cell, self.grid[j][i])


def randomized_grid(width, height):
    return [[random.choice([True, False]) for x in range(width)]
            for y in range(height)]
