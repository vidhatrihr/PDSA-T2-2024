def histogram(lst):
  count = {}
  for num in lst:
    if num in count:
      count[num] += 1
    else:
      count[num] = 1
  hist = [(num, count[num]) for num in count]

  hist.sort(key=lambda x: (x[1], x[0]))
  return hist


lst = eval(input())
print(histogram(lst))
