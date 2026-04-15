from dataclasses import dataclass


class BadClass:
    def __init__(self, my_list: list = []):
        self.my_list = my_list

    def append_one(self, val="New val"):
        self.my_list.append(val)


bad1 = BadClass()
bad2 = BadClass()

bad1.append_one("value from b1")

print(bad2.my_list)


class GoodClass:
    def __init__(self, my_list: list = None):
        self.my_list = [] if my_list is None else my_list

    def append_one(self, val="New val"):
        self.my_list.append(val)

better1 = GoodClass()
better2 = GoodClass()

better1.append_one("value from b1")

print(better2.my_list)
