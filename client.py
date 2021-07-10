import curses


def end_win():
    curses.endwin()


class Client:
    ESC = 27
    KEY_LEFT = curses.KEY_LEFT
    KEY_RIGHT = curses.KEY_RIGHT
    KEY_UP = curses.KEY_UP
    KEY_DOWN = curses.KEY_DOWN

    def __init__(self,lines, columns, y, x):
        curses.initscr()
        win = curses.newwin(lines, columns, y, x)
        win.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        win.border(0)
        win.nodelay(1)
        win.timeout(100)
        self.win = win

    def key_listener(self):
        return self.win.getch()

    def draw(self, num1, num2, word, test):
        if test == 1:
            self.win.addch(num1, num2, word)
        else:
            self.win.addstr(num1, num2, word)