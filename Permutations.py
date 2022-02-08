from itertools import permutations
count = 0
for c in permutations("0123456789", 10):
  # print("".join(c))
  a = "".join(c)
  index0 = a.find('0')
  index1 = a.find('1')
  index2 = a.find('2')
  index3 = a.find('3')
  index4 = a.find('4')
  index5 = a.find('5')
  index6 = a.find('6')
  index7 = a.find('7')
  index8 = a.find('8')
  index9 = a.find('9')

  if index0 < index2 < index4 < index6 < index8 and index1 < index3 < index5 < index7 < index9:
    count += 1

print(count)