class Restaurant():
    def __init__(self, restaurant_name, *cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name is {self.name.upper()}")
        print("Cuisine Type")
        i = 1
        for food in self.cuisine:
            print(f" {str(i)}. {food.title()}")
            i+=1
    
    def open_restaurant(self, message):
        print('Restaurant is ' + message.upper())

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant('take a bite', 'rice', 'fish', 'meat', 'dal')
restaurant.describe_restaurant()
restaurant.open_restaurant('open')
restaurant.set_number_served(100)
active = True
while active:
    customer = input("Total customer: ")
    if customer == 'closed':
        restaurant.open_restaurant(customer)
        active = False
    else:
        restaurant.increment_number_served(int(customer))
        print("Customers the restaurant has served: " + str(restaurant.number_served))

print("Customers the restaurant has served: " + str(restaurant.number_served))
