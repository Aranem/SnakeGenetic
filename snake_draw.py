import pygame
import snake_game_util
from snake import Snake


class SnakeDraw:
    def __init__(self, surface, font):
        self.surface = surface
        self.font = font

    def draw_score(self, score):
        score_surf = self.font.render('Score: %s' % score, True, snake_game_util.WHITE)
        score_rect = score_surf.get_rect()
        score_rect.topleft = (snake_game_util.WINDOWWIDTH - 120, 10)
        self.surface.blit(score_surf, score_rect)

    def draw_snake(self, snake):
        for segment in snake.body:
            x = segment.x * snake_game_util.CELLSIZE
            y = segment.y * snake_game_util.CELLSIZE
            segment_rect = pygame.Rect(x, y, snake_game_util.CELLSIZE, snake_game_util.CELLSIZE)
            pygame.draw.rect(self.surface, snake_game_util.DARKGREEN, segment_rect)
            inner_segment_rect = pygame.Rect(x + 4, y + 4, snake_game_util.CELLSIZE - 8, snake_game_util.CELLSIZE - 8)
            pygame.draw.rect(self.surface, snake_game_util.GREEN, inner_segment_rect)

    def draw_snack(self, coord):
        x = coord['x'] * snake_game_util.CELLSIZE
        y = coord['y'] * snake_game_util.CELLSIZE
        snack_rect = pygame.Rect(x, y, snake_game_util.CELLSIZE, snake_game_util.CELLSIZE)
        pygame.draw.rect(self.surface, snake_game_util.RED, snack_rect)

    def draw_grid(self):
        for x in range(0, snake_game_util.WINDOWWIDTH, snake_game_util.CELLSIZE):  # draw vertical lines
            pygame.draw.line(self.surface, snake_game_util.DARKGRAY, (x, 0), (x, snake_game_util.WINDOWHEIGHT))
        for y in range(0, snake_game_util.WINDOWHEIGHT, snake_game_util.CELLSIZE):  # draw horizontal lines
            pygame.draw.line(self.surface, snake_game_util.DARKGRAY, (0, y), (snake_game_util.WINDOWWIDTH, y))
