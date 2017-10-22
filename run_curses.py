import curses
from time import sleep
from model import Universe, randomized_grid
import argparse
import csv

parser = argparse.ArgumentParser(
    description='Curses version of Conway\'s Game of Life. Enjoy!')
parser.add_argument('--width', help='Universe width', type=int, default=80)
parser.add_argument('--height', help='Universe height.', type=int, default=22)
parser.add_argument('--bpm', help='Beats per minute', type=float, default=120)
parser.add_argument('--init', help='CSV initial state',
                    type=argparse.FileType('r'))
args = parser.parse_args()


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

    if args.init:
        u = []
        reader = csv.reader(args.init)
        for row in reader:
            bool_row = [True if n == '1' else False
                        for n in row]
            u.append(bool_row)
    else:
        u = randomized_grid(args.width, args.height)

    s = simulation(stdscr,
                   Universe(u))

    # initialize main loop
    delay = 60.0 / args.bpm

    while True:

        s.curses_render()
        s.step()
        # as time goes by
        sleep(delay)


curses.wrapper(main)
