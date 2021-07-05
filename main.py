from random import randint
from field_draw import *
import curses

draw_field(20, 60, 0, 0)
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)

win_add(food[0], food[1], '#', 1)

score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    win_add(0, 2, f'Score: {score}', 2)
    # draw_field(150 - (len(snake)) // 5 + len(snake) // 10 % 120)  # speed increase

    prev_key = key
    new_key = event()
    key = new_key if new_key != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    y = snake[0][0]
    x = snake[0][1]
    win_add(0, 11, f"x = {x} y = {y}", 2)
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_RIGHT:
        x += 1
    if key == curses.KEY_LEFT:
        x -= 1
    snake.insert(0, (y, x))  # append 0(n)

    if y in (0, 19):
        break
    if x in (0, 59):
        break

    if snake[0] in snake[1:]:
        break

    if snake[0] == food:
        score += 1
        food = ()
        while food == ():
            food = (randint(1, 18), randint(1, 58))
            if food in snake:
                food = ()
        win_add(food[0], food[1], '#', 1)
    else:
        last = snake.pop()
        win_add(last[0], last[1], ' ', 1)

    win_add(snake[0][0], snake[0][1], '*', 1)

end()
print(f'Final score : {score}')
