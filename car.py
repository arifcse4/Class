class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def describe_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it.")

    def update_odometer(self, milage):
        if milage > self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer.")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

car = Car('audi', 'a4', 2016)
ret = car.describe_name()
print(ret)
car.update_odometer(25)
car.read_odometer()
car.increment_odometer(10)
car.read_odometer()