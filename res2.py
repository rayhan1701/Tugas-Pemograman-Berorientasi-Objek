class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant (self):
        print (f"1. Nama Restoran : {self.restaurant_name}")
        print (f"2. Jenis Masakan : {self.cuisine_type}")

    def open_restaurant (self):
        print (f"{self.restaurant_name} telah dibuka")
        
    def increment_number_served(self,jumlah):
        self.number_served += jumlah
    
    def  set_number_served (self):
        print (f"jumlah pelanggan yang telah dilayani dalam 1 hari : {self.number_served}")
        print("-------------------------------------------")
        
resto1 = Restaurant("pizza hut", "italia")
resto2 = Restaurant("Kfc","fast food")
resto3 = Restaurant("ampera","padang")
print("-------------------------------------------")

resto1.open_restaurant()
resto1.describe_restaurant()
resto1.increment_number_served (100)
resto1.set_number_served()

resto2.open_restaurant()
resto2.describe_restaurant()
resto2.increment_number_served (100)
resto2.set_number_served()

resto3.open_restaurant()
resto3.describe_restaurant()
resto3.increment_number_served (100)
resto3.set_number_served()

class User:
    def __init__ (self,first_name, last_name): 
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        
    def describe_user (self):
        print (f"1. nama depan : {self.first_name}")
        print (f"2. nama belakang : {self.last_name}")

    def greet_user (self):
        print (f"selamat datang {self.first_name} {self.last_name} ")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        print (f"3. jumlah login : {self.login_attempts} ")
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print (f"4. jumlah login setelah direset : {self.login_attempts} ")
        print("-------------------------------------------")
        
user1 = User("raihan","gunawan")
user2 = User("salsa","aurelya")

user1.greet_user()
user1.describe_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()

user2.greet_user()
user2.describe_user()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.reset_login_attempts()
