import math

import pygame


class GameObject:
    """Барлық ойын объектілерінің ата-ана класы: координата (x, y) және өлшем."""

    # Оқ тиетін объектілер (нысана) үшін True болады
    hittable = False

    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.alive = True

    def update(self, game):
        """Әр кадрда шақырылады. Еншілес кластар қайта анықтайды."""

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def on_hit(self, game):
        """Оқ тигенде не болады. Тек hittable объектілер қайта анықтайды."""
