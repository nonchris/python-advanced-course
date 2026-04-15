for num in [128, -65]:
    print(f"# >> {num:<+7d} ==> {num:>11b}")

l = [2,  111]
my_str = "\n".join(f">> {i: <{len(str(max(l)))}}: x" for i in l)
print(my_str)


