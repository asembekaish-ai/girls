import random

import pygame

from game_object import GameObject


class Target(GameObject):
    """Нысана: экранда қозғалады, оқ тигенде жойылады."""

    hittable = True

    def __init__(self, width):
        super().__init__(random.randint(60, width - 60), random.randint(60, 300), 28, (220, 30, 30))
        self.speed_x = random.choice([-1, 1]) * random.randint(2, 4)

    def update(self, game):
        self.x += self.speed_x
        if self.x <= self.size or self.x >= game.width - self.size:
            self.speed_x *= -1

    def draw(self, screen):
        pos = (int(self.x), int(self.y))
        pygame.draw.circle(screen, (255, 0, 0), pos, 28)
        pygame.draw.circle(screen, (255, 255, 255), pos, 19)
        pygame.draw.circle(screen, (255, 0, 0), pos, 10)

    def on_hit(self, game):
        self.alive = False
        game.score.add(1)
        game.spawn_target()
