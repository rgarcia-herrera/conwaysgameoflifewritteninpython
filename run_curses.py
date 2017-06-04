import curses
from time import sleep
from model import Universe, randomized_grid


class simulation:

    def __init__(self, stdscr, universe):
        self.u = universe
        self.stdscr = stdscr

    def step(self):
        next_grid = [[self.u.grid[y][x].next_state()
                      for x in range(self.u.width)]
                     for y in range(self.u.height)]

        self.u = Universe(next_grid)

    def curses_render(self):
        active = curses.color_pair(1)
        inactive = curses.color_pair(2)

        for x in range(self.u.width):
            for y in range(self.u.height):
                if self.u.grid[y][x].active:
                    self.stdscr.addch(y, x,
                                      'x', active)
                else:
                    self.stdscr.addch(y, x,
                                      ' ', inactive)

        self.stdscr.refresh()


def main(stdscr):
    # initialize curses environment
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)
    stdscr.nodelay(1)

    s = simulation(stdscr,
                   Universe(randomized_grid(80, 24)))

    # initialize main loop
    bpm = 120
    delay = 60.0 / bpm

    while True:

        s.curses_render()
        s.step()
        # as time goes by
        sleep(delay)


curses.wrapper(main)
