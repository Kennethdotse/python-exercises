class item:
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def compute_price(self):
        return self.price * self.quantity

item1=item("laptop",10,250)
item2=item("car",2,50000)

print(item1.compute_price())

print(item1.quantity)
print(item1.name)
