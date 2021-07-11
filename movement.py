import curses
from client import Client

class Movement:
    def __init__(self, client):
        self.client = client
        self.prev_key = Client.KEY_RIGHT


    def handle_snake_step(self, snake, new_key):
        key = new_key if new_key != -1 else self.prev_key
        if key not in [Client.KEY_UP, Client.KEY_LEFT, Client.KEY_RIGHT, Client.KEY_DOWN]:
            key = self.prev_key

        y = snake[-1][0]
        x = snake[-1][1]

        if key == Client.KEY_DOWN:
            y += 1
        if key == Client.KEY_UP:
            y -= 1
        if key == Client.KEY_RIGHT:
            x += 1
        if key == Client.KEY_LEFT:
             x -= 1
        self.prev_key = key
        return x, y