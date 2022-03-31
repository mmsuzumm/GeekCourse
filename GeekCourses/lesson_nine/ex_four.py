class Car:
    def __init__(self, speed, color, name, is_police=bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The {self.name} went')

    def stop(self):
        print(f'The {self.name} stoped')

    def turn(self, direction):
        print(f'The {self.name} turned to {direction}')

    def show_speed(self):
        print(f'The speed is {self.speed} miles an hour')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Over speed')
        super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Over speed')


class PoliceCar(Car):
    pass


town_car = TownCar(90, 'blue', 'AAA', False)
sport_car = SportCar(240, 'red', 'BBB', False)
work_car = WorkCar(60, 'white', 'CCC', False)
police_car = PoliceCar(90, 'black', 'DDD', True)

town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('right')