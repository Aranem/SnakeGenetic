import snake_game_util


class Snake:
    class SnakeSquare:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def __init__(self, startx, starty):
        self.body = [Snake.SnakeSquare(startx, starty)]

        self.direction = snake_game_util.RIGHT

    @property
    def head(self):
        return self.body[0]

    def move(self, snack_eaten):
        # add a segment in the direction the snake is moving
        if self.direction == snake_game_util.UP:
            new_segment = Snake.SnakeSquare(self.head.x, self.head.y - 1)
        elif self.direction == snake_game_util.DOWN:
            new_segment = Snake.SnakeSquare(self.head.x, self.head.y + 1)
        elif self.direction == snake_game_util.LEFT:
            new_segment = Snake.SnakeSquare(self.head.x - 1, self.head.y)
        elif self.direction == snake_game_util.RIGHT:
            new_segment = Snake.SnakeSquare(self.head.x + 1, self.head.y)
        self.body.insert(0, new_segment)

        # remove last segment if a snack is not being eaten
        if not snack_eaten and len(self.body) > 1:
            del self.body[-1]

    def is_head_at_pos(self, x, y):
        if self.head.x == x and self.head.y == y:
            return True
        else:
            return False
