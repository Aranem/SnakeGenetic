import random, pygame, sys
from pygame.locals import *
from snake import Snake
from snake_draw import SnakeDraw
import snake_game_util


class SnakeGame:
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((snake_game_util.WINDOWWIDTH, snake_game_util.WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    def __init__(self):
        self.snake = Snake(random.randint(5, snake_game_util.CELLWIDTH - 6), random.randint(5, snake_game_util.CELLHEIGHT - 6))
        self.snake_drawer = SnakeDraw(DISPLAYSURF, BASICFONT)
        self.snack = None

    def run_game(self):
        # Start the snack in a random place.
        self.snack = self.get_random_location()

        while True:  # main game loop
            self.change_snake_direction()

            if self.check_snake_death() is True:
                return

            snack_eaten = self.check_snack_eaten()

            self.move_snake(snack_eaten)

            DISPLAYSURF.fill(snake_game_util.BGCOLOR)
            self.snake_drawer.draw_grid()
            self.snake_drawer.draw_snake(self.snake)
            self.snake_drawer.draw_snack(self.snack)
            self.snake_drawer.draw_score(len(self.snake.body))
            pygame.display.update()
            FPSCLOCK.tick(snake_game_util.FPS)

    def change_snake_direction(self):
        for event in pygame.event.get():  # event handling loop
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and self.snake.direction != snake_game_util.RIGHT:
                    self.snake.direction = snake_game_util.LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and self.snake.direction != snake_game_util.LEFT:
                    self.snake.direction = snake_game_util.RIGHT
                elif (event.key == K_UP or event.key == K_w) and self.snake.direction != snake_game_util.DOWN:
                    self.snake.direction = snake_game_util.UP
                elif (event.key == K_DOWN or event.key == K_s) and self.snake.direction != snake_game_util.UP:
                    self.snake.direction = snake_game_util.DOWN
                elif event.key == K_ESCAPE:
                    self.terminate()

    def check_snack_eaten(self):
        if self.snake.is_head_at_pos(self.snack['x'], self.snack['y']):
            self.snack = self.get_random_location()
            return True
        else:
            return False

    def move_snake(self, snack_eaten):
        self.snake.move(snack_eaten)

    def check_snake_death(self):
        # Check collision with body or game edge
        if self.snake.head.x == -1 or self.snake.head.x == snake_game_util.CELLWIDTH or self.snake.head.y == -1 or self.snake.head.y == snake_game_util.CELLHEIGHT:
            return True
        for body_square in self.snake.body[1:]:
            if body_square.x == self.snake.head.x and body_square.y == self.snake.head.y:
                return True

        return False

    def terminate(self):
        pygame.quit()
        sys.exit()

    def check_for_key_press(self):
        if len(pygame.event.get(QUIT)) > 0:
            self.terminate()

        key_up_events = pygame.event.get(KEYUP)
        if len(key_up_events) == 0:
            return None
        if key_up_events[0].key == K_ESCAPE:
            self.terminate()
        return key_up_events[0].key

    def get_random_location(self):
        return {'x': random.randint(0, snake_game_util.CELLWIDTH - 1), 'y': random.randint(0, snake_game_util.CELLHEIGHT - 1)}
