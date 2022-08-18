from random import randint


class Dice:
    """Класс кубика"""
    def __init__(self, num_sides=6):
        """Инициализация количества сторон кубика"""
        self.num_sides = num_sides

    def roll(self):
        """Бросок кубика"""
        return randint(1, self.num_sides)
