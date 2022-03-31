import time


class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 5), ('Yellow', 2), ('Green', 4))  # атрибут реализовать как приватный;

    def running(self):
        while True:
            for color, sec in self.__color:
                print(color)
                time.sleep(sec)


light = TrafficLight()
light.running()