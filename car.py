class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

car = Car('audi', 'a4', 2016)
ret = car.describe_name()
print(ret)