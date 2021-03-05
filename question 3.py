class Product:
    def __init__(self,product_id="",product_name="",product_purchase_price=0,product_sale_price=0):
        self.product_id=product_id
        self.product_name=product_name
        self.product_purchase_price=product_purchase_price
        self.product_sale_price=product_sale_price

    def set_remarks(self):
        self.margin=self.product_sale_price-self.product_purchase_price
        if self.margin<0:
            self.remarks="Loss"
        else:
            self.remarks="Profit"
        return self.remarks

    def get_details(self):
        self.product_id=input("Enter product id:")
        self.product_name=input("Enter product name:")
        self.product_purchase_price=input("Enter purchase price:")
        self.product_sale_price=input("Enter sale price:")

    def set_details(self):
        print(f"""
Product id:{self.product_id}
Product name:{self.product_name}
Purchase price:{self.product_purchase_price}
Sale price:{self.product_sale_price}
Margin:{self.margin}
Remarks:{self.remarks}""")


a=Product()
a.set_remarks()
a.get_details()
a.set_details()