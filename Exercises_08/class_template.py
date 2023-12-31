class MySimpleClass:
    """
    A simple class template with two methods.
    """

    def __init__(self, attribute1: str, attribute2: bool):
        """
        Constructor for MySimpleClass.

        Parameters:
        - attribute1 (str): A string attribute.
        - attribute2 (bool): A boolean attribute.
        """
        self.attr1 = attribute1
        self.attr2 = attribute2

    def my_method1(self):
        """
        Greet the user based on the 'attr2' attribute.

        If 'attr2' is True, it says 'Good morning [attr1]'.
        If 'attr2' is False, it says 'No greeting [attr1]'.
        """
        if self.attr2:
            print(f"Good morning {self.attr1}")
        else:
            print(f"No greeting {self.attr1}")

    def my_method2(self, my_name: str):
        """
        Greet a user with a custom name.

        If 'attr2' is True, it says 'Good morning [my_name]'.
        If 'attr2' is False, it says 'No greeting [my_name]'.

        Parameters:
        - my_name (str): A custom name to greet.
        """
        if self.attr2:
            print(f"Good morning {my_name}")
        else:
            print(f"No greeting {my_name}")

