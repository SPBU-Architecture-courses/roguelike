import pygame
from package.engine.engine import Engine
from package.engine.render.renderEntity import RenderEntity

SCREEN_COLOR = (255, 255, 255)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

class GameWindow:
    """
    Инициализирует начало игры и отрисовывает все объекты на поле.
    """
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Roguelike")

        Engine.start()

        self.screen.set_alpha(None)
        self.running = True

        print("GameWindow: Created game window")

    def run(self):
        """
        Основной игровой цикл.
        """
        clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.handle_keydowns(pygame.key.get_pressed())

            self.render()

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()


    def handle_keydowns(self, keys):
        protagonist = Engine.get_protagonist()
        move_distance = 5
        if keys[pygame.K_LEFT]:
            protagonist.set_pos(protagonist.x - move_distance, protagonist.y)
        if keys[pygame.K_RIGHT]:
            protagonist.set_pos(protagonist.x + move_distance, protagonist.y)
        if keys[pygame.K_UP]:
            protagonist.set_pos(protagonist.x, protagonist.y - move_distance)
        if keys[pygame.K_DOWN]:
            protagonist.set_pos(protagonist.x, protagonist.y + move_distance)

    def render(self):
        """
        Отрисовывает все элементы на экране.
        """
        self.screen.fill((0, 0, 0))

        WHITE = (255, 255, 255)
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(15, 15, SCREEN_WIDTH - 30, SCREEN_HEIGHT - 30))

        protagonist = Engine.get_protagonist()
        RenderEntity.render(protagonist, self.screen)
