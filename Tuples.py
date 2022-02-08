from itertools import product

for c in product("abc", repeat=2):
  print("".join(c))