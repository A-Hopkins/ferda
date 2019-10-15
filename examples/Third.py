"""
This is the third example. This example is an introductory lesson into
object-oriented programming (OOP). Object-oriented programming is a programming paradigm based on the concept of
"objects", which can contain data, in the form of fields, and code, in the form of procedures.

What that means is in code you would have an object, Plant, that contains information about the Plant, like height,
color and you have functions that control those fields of data. Like grow() to increase height.

The usefulness of OOP is to encapsulate your data so things you don't expect to modify it cannot modify the information.
It is also useful to hide data.

Created by alex
"""


# This is a class. A Class is how you create and define the object.
class Plant:
    """
    Plant class to characterize a plant.
    """

    def __init__(self, size, color, leaves):
        """
        This is the initialize function. In here the object gets initialized when it is called into the scope with these
        values and it must be initialized with the parameters size, color, and leaves.

        :param size: The size of the plant (small, med, large)
        :param color: Color of the plant
        :param leaves: If the plant has leaves or not (True or False)
        """
        self.size = size
        self.color = color
        self.leaves = leaves
        self.height = 0

    def grow(self, growth):
        """
        This function is a method that acts on the data of the plant class. It makes the plant grow!

        :param growth: The amount the plant should grow by
        """

        self.height += growth


# To initialize an object you have to call it by setting it to a variable and calling it like so
# We have made an object called fern of the type Plant, it is represented as a small green plant with leaves
fern = Plant("small", "green", True)

# If you want to see some of the data of fern you can print it like this:
print(fern.height)  # We see that the height of the fern is 0! Let's make it grow.

# If we want fern to grow we use the method grow on it like so
fern.grow(9)    # We grow it by 9 units
print(fern.height)

"""
Now for the challenge. You have just learned how to create a class and some methods that alter the data of the class.

Design an object of your own and give it some methods to interact with that object.
"""
