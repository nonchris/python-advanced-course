import numpy as np

class MyClass:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f"MyClass({self.x})"


# Create instances of MyClass
instances = np.array([MyClass(1), MyClass(2), MyClass(3)])

# Create a new copy of the instances array using np.array()
instances_copy = np.array(instances)

# mutate the data in the copy
instances_copy[0].x = "hey"

# print the objects value x
print(instances_copy[0].x)
print(instances[0].x)
