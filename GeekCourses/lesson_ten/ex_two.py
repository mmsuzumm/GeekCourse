from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):
    @property
    def calc(self):
        return round((self.param / 6.5) + 0.5)


class Suit(Clothes):
    @property
    def calc(self):
        return round((2 * self.param)+ 0.3)

coat = Coat(55)
suit = Suit(155)
print(coat.calc)
print(suit.calc)