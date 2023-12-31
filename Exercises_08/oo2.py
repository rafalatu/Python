"""
Class template by RAFAL

Revision History
27OCT22: Alpha
28OCT23: Beta
"""

class MyTemplate():
    # Constructor, called whenever an instance of the class is created.
    def __init__(self) -> None:
        print("Constructor ran")

# Instantiate the class
my_object = MyTemplate("John", True)
# Check the object and type
print(type(my_object))

# Constructor, called whenever an instance of the class is created.
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran")
        # Take in an argument and assign it to a meaningful attribute name
        self.attr1 = attribute1
        self.attr2 = attribute2

   # Define a class object attribute, it will be the same for any instance of the class
    class_object_attribute1 = 6378137
    class_object_attribute2 = 6356752 

        # Instantiate the class
my_object = MyTemplate("John", True)
# Check the object
print(my_object.semi_major_axis, my_object.semi_minor_axis)