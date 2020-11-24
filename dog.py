class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        print(f"{self.name.title()} rolled over!!!")

my_dog = Dog('willi', 3)

print(f"My dog name is {my_dog.name.title()}.")
print(f"My dog is {str(my_dog.age)} years old.")
my_dog.sit()
my_dog.roll_over()
