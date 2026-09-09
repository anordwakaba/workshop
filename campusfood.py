class Menuitem:
    def __init__(self, name, price, ):
        self.name = name
        self.price = price
       

    def __str__(self):
        return f"{self.name} - {self.price:.2f}: {self.description}"

class customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def order(self, menu_item):
        if self.balance >= menu_item.price:
            self.balance -= menu_item.price
            print(f"{self.name} ordered {menu_item.name}. Remaining balance: {self.balance:.2f}")
        else:
            print(f"{self.name} does not have enough balance to order {menu_item.name}.")

class order:
    def __init__(self, customer, menu_item):
        self.customer = customer
        self.menu_item = menu_item

    def add_item(self, menu_item):
        self.menu_item = menu_item
        print(f"{self.customer.name} added {menu_item.name} to the order.") 

    def calculate_total(self):
        return self.menu_item.price

    def show_order(self):
        print(f"Order for {self.customer.name}: {self.menu_item.name} - {self.menu_item.price:.2f}")

Burger = Menuitem("Burger", 370)
Pizza = Menuitem("Pizza", 850) 
Kachumbari = Menuitem("Kachumbari", 100)    

customer1 = customer("John", 1000)
order1 = order(customer1, Burger)

order1.add_item(Pizza) 
order1.add_item(Kachumbari)
order1.add_item(Burger)

order1.show_order()