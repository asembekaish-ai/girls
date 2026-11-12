import pygame

from player import Player
from score import Score
from target import Target

WIDTH = 800
HEIGHT = 650
FIELD_HEIGHT = 600
GAME_TIME = 60
WIN_SCORE = 20
TARGET_COUNT = 4


class Game:
    """Ойынның негізгі класы: терезе, цикл, ұпай, уақыт, жеңу мен жеңілу."""

    def __init__(self):
        pygame.init()
        self.width = WIDTH
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("2D ТИР")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 24, bold=True)
        self.big_font = pygame.font.SysFont("arial", 44, bold=True)
        self.small_font = pygame.font.SysFont("arial", 22)
        self.keys = pygame.key.get_pressed()
        self.restart()

    def restart(self):
        self.score = Score(WIN_SCORE)
        self.time_left = float(GAME_TIME)
        self.state = "playing"  # playing / won / lost
        self.player = Player(WIDTH // 2, FIELD_HEIGHT - 30)
        # Әртүрлі класс объектілері (ойыншы, нысаналар, оқтар) бір тізімде тұрады
        self.objects = [self.player]
        for _ in range(TARGET_COUNT):
            self.spawn_target()

    def spawn_target(self):
        self.objects.append(Target(WIDTH))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.restart()
                elif event.key == pygame.K_SPACE and self.state == "playing":
                    self.objects.append(self.player.shoot())
        return True

    def update(self, dt):
        if self.state != "playing":
            return

        self.keys = pygame.key.get_pressed()
        self.time_left -= dt

        for obj in list(self.objects):
            obj.update(self)
        self.objects = [obj for obj in self.objects if obj.alive]

        if self.score.reached_goal():
            self.state = "won"
        elif self.time_left <= 0:
            self.time_left = 0
            self.state = "lost"

    def draw(self):
        self.screen.fill((32, 32, 32))
        pygame.draw.rect(self.screen, (114, 184, 91), (0, 0, WIDTH, FIELD_HEIGHT))
        pygame.draw.rect(self.screen, (121, 85, 72), (0, FIELD_HEIGHT - 12, WIDTH, 12))

        for obj in self.objects:
            obj.draw(self.screen)

        self.draw_hud()
        if self.state != "playing":
            self.draw_result()
        pygame.display.flip()

    def draw_hud(self):
        white = (255, 255, 255)
        score = self.font.render(f"Ұпай: {self.score.points}/{WIN_SCORE}", True, white)
        timer = self.font.render(f"Уақыт: {int(self.time_left)}", True, white)
        hint = self.small_font.render("← →: жүру   SPACE: ату   R: қайта бастау", True, (200, 200, 200))
        self.screen.blit(score, (30, FIELD_HEIGHT + 8))
        self.screen.blit(timer, (620, FIELD_HEIGHT + 8))
        self.screen.blit(hint, (30, FIELD_HEIGHT + 40))

    def draw_result(self):
        box = pygame.Rect(150, 170, 500, 200)
        pygame.draw.rect(self.screen, (255, 255, 255), box)
        pygame.draw.rect(self.screen, (0, 0, 0), box, 3)

        if self.state == "won":
            title, color = "ЖЕҢІСТІ!", (0, 150, 0)
        else:
            title, color = "ЖЕҢІЛДІҢ!", (200, 0, 0)

        title_img = self.big_font.render(title, True, color)
        score_img = self.font.render(f"Нәтиже: {self.score.points}", True, (0, 0, 0))
        hint_img = self.small_font.render("Қайта бастау үшін R басыңыз", True, (0, 0, 200))
        self.screen.blit(title_img, title_img.get_rect(center=(400, 220)))
        self.screen.blit(score_img, score_img.get_rect(center=(400, 285)))
        self.screen.blit(hint_img, hint_img.get_rect(center=(400, 335)))

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(50) / 1000
            running = self.handle_events()
            self.update(dt)
            self.draw()
        pygame.quit()
