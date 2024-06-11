class Vehicle:
    wheels: int
    
    def __init__(self, speed):
        self.speed = speed
    
    @staticmethod
    def move():
        print(f'{self.__class__.__name__} двигается по земле со скоростью {self.speed} км/ч')


class Bicycle(Vehicle):
    wheels = 2


class Car(Vehicle):
    wheels = 4
    
    @staticmethod
    def move():
        print(f'{self.__class__.__name__} двигается по дороге со скоростью {self.speed} км/ч')


class Train(Vehicle):
    wheels = 12
    
    @staticmethod
    def move():
        print(f'{self.__class__.__name__} двигается по рельсам со скоростью {self.speed} км/ч')


class Aircraft(Vehicle):
    wheels = 6
    
    def __init__(self, ground_speed, air_speed):
        # пример некорректного использования наследования
        self.ground_speed = ground_speed
        self.air_speed = air_speed
    
    @staticmethod
    def move():
        print(f'{self.__class__.__name__} двигается по земле со скоростью {self.ground_speed} км/ч и в воздухе со скоростью {self.air_speed} км/ч')


vehicles = [
    Car(60),
    Bicycle(16),
    Car(90),
    Train(110),
    Aircraft(50, 500)
]
for vehicle in vehicles:
    print(f'{vehicle.speed = }')

# vehicle.speed = 60
# vehicle.speed = 16
# vehicle.speed = 90
# vehicle.speed = 110
# AttributeError: 'Aircraft' object has no attribute 'speed'

