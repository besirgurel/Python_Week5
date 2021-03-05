class Customer:
    def __init__(self,name,surname,customer_id):
        self.name=name
        self.surname=surname
        self.customer_id=customer_id
    def __str__(self):
        return print(f"""
Name: {self.name}
Surname: {self.surname}
Id number: {self.customer_id}""")

    def get_info(self):
        return self.customer_id

class Items:
    def __init__(self):
        self.customer_id=""
        self.price=0
        self.qty=0
        self.discount=0
    def __str__(self):
        return print(f"""
Shopping cart items: {self.shopping_basket}
Total price: {self.price_tobe_paid}""")

    def calculate_discount(self):
        if self.total_price>=4000:
            self.discount=self.total_price*0.25
            return self.discount
        elif 2000<=self.total_price>4000:
            self.discount=self.total_price*0.15
            return self.discount
        elif self.total_price<2000:
            self.discount=self.total_price*0.10
            return self.discount
    def shopping_cart(self):
        self.list_of_items={"pot":25,"teapot":15,"tv":800,"computer":1500,"book":5,"notebook":2,"pencil":1,"food processor":300}
        self.total_price=0
        self.shopping_basket=[]
        print(f"Items to be purchased:\n{list(self.list_of_items.keys())}")
        self.shopping_list=input("Create a shopping list with commas between them:\n").split(",")
        for i in self.shopping_list:
            self.shopping_basket.append(i)
            self.total_price+=self.list_of_items[i]
        return self.total_price

    def get_total_amount(self):
        self.price_tobe_paid=self.total_price-self.discount
        return self.price_tobe_paid
customer1=Customer("Besir","Gurel",26)

item1=Items()
item1.shopping_cart()
item1.calculate_discount()
item1.get_total_amount()
customer1.__str__()
item1.__str__()