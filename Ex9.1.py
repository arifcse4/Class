class Restaurant():
    def __init__(self, restaurant_name, *cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name is {self.name.upper()}")
        print("Cuisine Type")
        i = 1
        for food in self.cuisine:
            print(f"{str(i)}. {food.title()}")
            i+=1
    
restaurant = Restaurant('take a bite', 'rice', 'fish', 'meat', 'dal')
restaurant.describe_restaurant()
