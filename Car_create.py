class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed


my_car = Car('MyCar', 0)

my_car.accelerate()
my_car.accelerate()
my_car.brake()

current_speed = my_car.get_speed()
print(f"Your current speed is: {current_speed}")
