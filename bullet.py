import pygame

from game_object import GameObject


class Bullet(GameObject):
    """Оқ: жоғары қарай ұшады, нысанаға тигенін тексереді."""

    def __init__(self, x, y):
        super().__init__(x, y, 5, (255, 220, 0))
        self.speed_y = -12

    def update(self, game):
        self.y += self.speed_y

        for obj in game.objects:
            if obj.hittable and obj.alive and self.distance_to(obj) <= obj.size + self.size:
                obj.on_hit(game)
                self.alive = False
                return

        if self.y < 0:
            self.alive = False

    def draw(self, screen):
        pos = (int(self.x), int(self.y))
        pygame.draw.circle(screen, self.color, pos, self.size)
        pygame.draw.circle(screen, (0, 0, 0), pos, self.size, 1)
