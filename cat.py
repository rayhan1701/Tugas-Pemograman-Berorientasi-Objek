class Cat:
    """A simple attempt to model a cat"""

    def __init__ (self, name, age): #harus memakai parameter untuk input variabel dan diurutan pertama fungsi
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit (self):
        """Simulate a cat sitting in response to a command."""
        print (f"{self.name} is now sitting.")

    def roll_over (self):
        """Simulate rolling over in response to a command."""
        print (f"{self.name} rolled over!")
    
my_cat = Cat('L', 9)

print(f"My cat's name is {my_cat.name}.")
print(f"My cat is {my_cat.age} years old.")
my_cat.sit()
my_cat.roll_over()

your_cat = Cat('Mogi', 7)

print(f"Your cat's name is {your_cat.name}.")
print(f"Your cat is {your_cat.age} years old.")
your_cat.sit()
your_cat.roll_over()