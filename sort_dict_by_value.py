d = {'a':10, 'b': 1, 'c': 22}
tmp = []
for k, v in d.items():
  tmp.append((v,k))
print(sorted(tmp, reverse=True))

"""
if we could construct a list of tuples
of the form (value, key) we could sort by value

we do this with a for loop that creates a list 
of tuples

"""
