class MyClass:
    def __getitem__(self, item: int | slice):
        if type(item) is int:
            print("Just one index")

        else:
            item : slice
            print(item.start)
            print(item.stop)
            print(item.step)

if __name__ == '__main__':

    m = MyClass()
    # m[4]
    m[1:6]

    slc = slice(1, 5, 2)
    print(slc)
    m[slc]

    l = list(range(10))
    print(l[slc])


