slc = slice(1, 6, 2)
my_list = list(range(10))
res1 = my_list[slc]
res2 = my_list[slc.start: slc.stop: slc.step]

print(res1)
print(res2)
print(res2)