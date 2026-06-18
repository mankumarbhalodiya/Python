class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()

    def discount(self, percent):
        self.price = self.price - (self.price * percent / 100)

# create two books
b1 = Book("Python Basics", "Amit", 500)
b2 = Book("C++ Guide", "Riya", 700)

print("Before Discount:")
b1.show_details()
b2.show_details()

b2.discount(10)

print("After 10% Discount:")
b1.show_details()
b2.show_details()
