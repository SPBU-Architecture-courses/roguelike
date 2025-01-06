import pygame
from package.protagonist.protagonist import Protagonist

class Engine:
    """
    Класс Engine управляет состоянием игры, включая персонажа и игровой цикл.
    """

    _protagonist = None 
    _clock = None 

    @classmethod
    def start(cls):
        """
        Инициализирует игру, создаёт персонажа и устанавливает начальные параметры.
        """
        cls._protagonist = Protagonist(20, 200, 200)
        cls._clock = pygame.time.Clock()
        print("Engine: Игра инициализирована.")

    @classmethod
    def move_protagonist(cls, dX: int, dY: int) -> None:
        """
        Передвигает персонажа на заданное количество пикселей по оси X и Y.

        :param dX: Перемещение по оси X
        :param dY: Перемещение по оси Y
        """
        if cls._protagonist:
            new_x = cls._protagonist.x + dX
            new_y = cls._protagonist.y + dY
            cls._protagonist.set_pos(new_x, new_y)
            print(f"Engine: Персонаж перемещён на ({dX}, {dY}) к новой позиции ({new_x}, {new_y}).")

    @classmethod
    def get_protagonist(cls) -> Protagonist:
        """
        Возвращает экземпляр персонажа.

        :return: Экземпляр класса Protagonist
        """
        return cls._protagonist
