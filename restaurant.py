class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant (self):
        print (f"1. Nama Restoran : {self.restaurant_name}")
        print (f"2. Jenis Masakan : {self.cuisine_type}")

    def open_restaurant (self):
        print (f"{self.restaurant_name} telah dibuka")

resto1 = Restaurant("pizza hut", "italia")
resto2 = Restaurant("Kfc","fast food")
resto3 = Restaurant("ampera","padang")
print("-------------------------------------------")
resto1.open_restaurant()
resto1.describe_restaurant()
resto2.open_restaurant()
resto2.describe_restaurant()
resto3.open_restaurant()
resto3.describe_restaurant()

class User:
    def __init__ (self,first_name, last_name): 
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user (self):
        print (f"1. nama depan : {self.first_name}")
        print (f"2. nama belakang : {self.last_name}")

    def greet_user (self):
        print (f"selamat datang {self.first_name} {self.last_name} ")
        
user1 = User("raihan","gunawan")
user2 = User("salsa","aurelya")
print("-------------------------------------------")
user1.greet_user()
user1.describe_user()
user2.greet_user()
user2.describe_user()
print("-------------------------------------------")