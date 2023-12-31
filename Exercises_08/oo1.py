"""
Simple Class by RAFAL, by convention, use camel case to name classes
"""

# Create a class 
class RAFALzClass():
    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for JORzClass")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)

my_class1 = RAFALzClass("Morning RAFAL")
my_class1.my_method()
print(type(my_class1))

class MyClass2:
    def __init__(self, my_greeting):
        print("Running constructor for MyClass2")
        self.message = my_greeting

    def my_method(self):
        print(self.message)

# Creating an instance of MyClass2
my_class2 = MyClass2("Hello from RAFAL")
my_class2.my_method()
print(type(my_class2))

from oo1 import MyClass2

# CreatING an instance of MyClass2
my_class2 = MyClass2("Hello from RAFAL")
my_class2.my_method()
print(type(my_class2))

