class Protagonist:
    """
    Характеристики персонажа и методы, связанные с его перемещением
    """

    def __init__(self, hit_points: int, x: int, y: int):
        self._hit_points = hit_points
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def set_pos(self, new_x: int, new_y: int) -> None:
        """
        Устанавливает новую позицию персонажа.

        :param new_x: новая координата x
        :param new_y: новая координата y
        """
        self._x = new_x
        self._y = new_y

    @property
    def hit_points(self) -> int:
        return self._hit_points

    def set_hit_points(self, amount: int) -> None:
        """
        Уменьшает количество очков здоровья на 1.

        :param amount: (параметр не используется)
        """
        self._hit_points -= 1
