class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name, quantity):
        if dish_name in self.menu:
            dish = self.menu[dish_name]
            if quantity <= dish['quantity']:
                total_cost = dish['price'] * quantity
                dish['quantity'] -= quantity
                return total_cost
            else:
                return "Requested quantity is not availiable"
        else:
            return "The dish is not availiable"
    

menu = {
    'french fries': {'price': 3, 'quantity': 20},
    'hamburger': {'price': 5, 'quantity': 10},
    'coke': {'price': 2, 'quantity': 15}
}

ff_menu = FastFood('Mc_Dnlds', 'Fast Food', menu, True)

print(ff_menu.order('hamburger', 5))
print(ff_menu.order('french fries', 25))
print(ff_menu.order('coke', 10))
print(ff_menu.order('coke', 5))
