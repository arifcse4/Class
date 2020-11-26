class Restaurant():
    def __init__(self, restaurant_name, *cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name is {self.name.upper()}")
        print("Cuisine Type")
        i = 1
        for food in self.cuisine:
            print(f" {str(i)}. {food.title()}")
            i+=1
    
    def open_restaurant(self, message):
        print('Restaurant is ' + message.upper())


restaurant = Restaurant('take a bite', 'rice', 'fish', 'meat', 'dal')
restaurant.describe_restaurant()
restaurant.open_restaurant('open')

restaurant2 = Restaurant("Al Kaderia", 'fride chicken', 'nan', 'morog polao')
restaurant2.describe_restaurant()
restaurant2.open_restaurant('closed')

restaurant3 = Restaurant('red chili', 'bargur', 'coffee', 'pizza')
restaurant3.describe_restaurant()
restaurant3.open_restaurant('closed')

