class ItemInfo:
    def __init__(self):
        self.item_code=0
        self.item=""
        self.price=0
        self.qty=""
        self.discount=0
        self.net_price=0

    def buy(self):
        self.item_code=input("Enter item code:")
        self.item=input("Enter item name:")
        self.price=float(input("Enter price:"))
        self.qty=int(input("Enter quantity:"))

    def calculate_discount(self):
        if self.qty<=10:
            self.discount=0
        elif 10<self.qty<20:
            self.discount=15
        else:
            self.discount=20
        self.net_price=self.price*self.qty-self.discount

    def show_all(self):
        print(f"""
Item code:{self.item_code}
Item name:{self.item}
Price:{self.price}
Net price:{self.net_price}""")

a=ItemInfo()
a.buy()
a.calculate_discount()
a.show_all()