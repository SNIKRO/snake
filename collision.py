
class Collision:
    def __init__(self, client):
        self.client = client

    def snake_crash(self, snake, y, x):
        if (y, x) in snake[:-1]:
            return True
        client_height, client_width = self.client.win.getmaxyx()
        if y in (0, client_height) or x in (0, client_width):
            return True
        return False