from itertools import combinations

for c in combinations("abc", 2):
  print("".join(c))