def shuffle(l1, l2):
  result = []
  min_length = min(len(l1), len(l2))

  for i in range(min_length):
    result.append(l1[i])
    result.append(l2[i])

  result.extend(l1[min_length:])
  result.extend(l2[min_length:])

  return result


l1 = eval(input())
l2 = eval(input())

print(shuffle(l1, l2))
