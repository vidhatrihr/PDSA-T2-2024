def sumsquare(l):
  even = 0
  odd = 0
  for i in l:
    if i % 2 == 0:
      even += i**2
    else:
      odd += i**2

  return [odd, even]


l = eval(input())
print(sumsquare(l))
