import networkx as nx


class Cell:
    active = False

    def __init__(self, universe):
        self.u = universe

    def update(self):
        # death by isolation
        if self.active and self.active_neighbors() < 2:
            self.active = False

        # keep on truckin'
        if self.active and self.active_neighbors() == 2 \
           or self.active_neighbors() == 3:
            self.active = True

        # death by crowding
        if self.active and self.active_neighbors() > 3:
            self.active = False

        # be born!
        if not self.active and self.active_neighbors() == 3:
            self.active = True

    def active_neighbors(self):
        return sum([1 if n.active else 0 for n in self.u.g.neighbors(self)])


class Universe:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell(universe=self) for x in range(width)]
                     for y in range(height)]

        self.g = nx.Graph()
        self.tangle()

    def tangle(self):
        """ creates edges in network, connects neighbors together """
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                cell = self.grid[x][y]

                # connect to neighborhood
                for i in [x-1, x, x+1 if x+1 < self.width else -1]:
                    for j in [y-1, y, y+1 if y+1 < self.height else -1]:
                        self.g.add_edge(cell, self.grid[i][j])
