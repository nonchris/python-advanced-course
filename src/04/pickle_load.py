import pickle

from pickle_dump import PickleClass

x = 41

PickleClass.class_var = "newcv"
with open("pkl_file.pkl", "rb") as f:
    obj = pickle.load(f)

obj.say_global_var_x()
obj.say_data()
print(obj.class_var)

x = 43
obj.say_global_var_x()
