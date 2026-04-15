import pickle


class PickleClass:
    class_var = "cv"
    def __init__(self, data):
        self.data = data

    def say_global_var_x(self):
        print(x)

    def say_data(self):
        print(self.data)

x = 42
obj = PickleClass(69)
# obj.say_data = lambda : print("Wheeeee")

# file needs to be opened in byte mode
with open("pkl_file.pkl", "wb") as f:
    pickle.dump(obj, f)
