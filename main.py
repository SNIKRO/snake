from random import randint

from client import Client, end_win
from movement import Movement

client = Client(20, 60, 0, 0)
movement = Movement(client)
snake = [(4, 8), (4, 9), (4, 10)]
food = (10, 20)

score = 0

key = None

while key != Client.ESC:
    key = client.key_listener()
    x, y = movement.handle_snake_step(snake, key)
    if (y, x) in snake[:-1]:
        break
    if y in (0, 19) or x in (0, 59):
        break
    snake.append((y, x))  # append 0(n)

    if snake[-1] == food:
        score += 1
        food = None
        while food is None:
            food = (randint(1, 18), randint(1, 58))
            if food in snake:
                food = None
    else:
        tail = snake.pop(0)
        client.draw(tail[0], tail[1], ' ', 1)

    client.draw(0, 2, f'Score: {score}', 2)
    client.draw(food[0], food[1], '#', 1)

    client.draw(snake[-1][0], snake[-1][1], '*', 1)

end_win()
if key == Client.ESC:
    print("Game Over")
else:
    print("You lose")
print(f'Final score : {score}')
