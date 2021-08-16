from random import randint


class Die():
    """Class representing 1 die"""
    def __init__(self, num_sides=6):
        """The default is a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """"Returns a random number between 1 and the number of faces."""
        return randint(1, self.num_sides)

