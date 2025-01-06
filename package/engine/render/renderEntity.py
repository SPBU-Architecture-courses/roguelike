import pygame
from package.protagonist.protagonist import Protagonist
import package.engine.constants as constants

class RenderEntity:
    """
    Кастомная отрисовка персонажа.
    """
    @staticmethod
    def render(protagonist : Protagonist, surface):
        """
        Отрисовывает персонажа на заданной поверхности.

        :param protagonist: Объект типа Protagonist, который присутствует на карте.
        :param surface: Поверхность Pygame, на которую отрисовываем (например, экран).
        """
        pygame.draw.circle(surface, constants.PERSON_COLOR, (protagonist.x, protagonist.y), constants.PERSON_RADIUS)
   
