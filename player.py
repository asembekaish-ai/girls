import pygame

from bullet import Bullet
from game_object import GameObject


class Player(GameObject):
    """Ойыншы: солға және оңға қозғалады, оқ атады."""

    def __init__(self, x, y):
        super().__init__(x, y, 25, (40, 90, 200))
        self.speed = 6

    def update(self, game):
        keys = game.keys
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        # Экран шекарасынан шықпайды
        self.x = max(self.size, min(game.width - self.size, self.x))

    def shoot(self):
        """Жаңа оқ жасап қайтарады: оқ ойыншының ұңғысынан шығады."""
        return Bullet(self.x, self.y - 35)

    def draw(self, screen):
        body = pygame.Rect(0, 0, self.size * 2, 22)
        body.center = (int(self.x), int(self.y))
        pygame.draw.rect(screen, self.color, body, border_radius=4)
        barrel = pygame.Rect(0, 0, 8, 26)
        barrel.midbottom = (int(self.x), int(self.y) - 8)
        pygame.draw.rect(screen, (30, 30, 30), barrel)
