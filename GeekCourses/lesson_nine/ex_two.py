class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculator(self):
        return f'{int(self.__width * self.__length * 25 * 5/1000)} т'


mass_calc = Road(20, 5000)
print(mass_calc.calculator())