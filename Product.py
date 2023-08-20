class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name, autor, price, quantity):
        super().__init__(name, price, quantity)
        self.autor = autor

    def read(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.autor}")
        print(f"Price tag: {self.price}")
        print(f"Quantity: {self.quantity}")


book = Book("1986", "George Orwell", 13, 50)

book.read()
