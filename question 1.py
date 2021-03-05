class society:
    def __init__(self):
        self.society_name="Besir Apartment"
        self.house_no_of_mem=3
        self.flat="A type"
        self.income=25000
    def input_data(self):
        self.society_name=input("Enter society name:")
        self.house_no_of_mem=int(input("Enter house no of members:"))
        self.income=float(input("Enter income:"))
    def allocate_flat(self):
        if self.income>=25000:
            self.flat="A type"
        elif 25000>self.income>=20000:
            self.flat="B type"
        elif 20000>self.income>=15000:
            self.flat="C type"
        else:
            self.flat="D type"
    def show_data(self):
        print(f"""
Society name: {self.society_name}
House no of members: {self.house_no_of_mem}
Income: {self.income}
Flat type: {self.flat}""")
a=society()
a.input_data()
a.allocate_flat()
a.show_data()