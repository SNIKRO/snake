import curses


def draw_field(lines, colums, y, x):
    curses.initscr()
    global win
    win = curses.newwin(lines, colums, y, x)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)
    win.timeout(100)


def end():
    curses.endwin()


def win_add(num1, num2, word, test):
    if test == 1:
        win.addch(num1, num2, word)
    else:
        win.addstr(num1, num2, word)


def event():
    return win.getch()
