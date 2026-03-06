class Cat:
    """A simple attempt to model a cat"""

    def init (self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit (self):
        """Simulate a cat sitting in response to a command."""
        print (f"(self.name) is now sitting.")

    def roll_over (self):
     """Simulate rolling over in response to a command."""
     print (f"(self.name) rolled over!")