from random import randint

from client import Client, end_win
from movement import Movement

client = Client(20, 60, 0, 0)
movement = Movement(client)
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)

score = 0

key = None

while key != Client.ESC:
    key = client.key_listener()
    x, y = movement.handle_snake_step(snake, key)
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

    else:
        last = snake.pop()

    client.draw(0, 2, f'Score: {score}', 2)
    client.draw(food[0], food[1], '#', 1)
    client.draw(last[0], last[1], ' ', 1)
    client.draw(snake[0][0], snake[0][1], '*', 1)

end_win()
if key == Client.ESC:
    print("Game Over")
else:
    print("You lose")
print(f'Final score : {score}')
