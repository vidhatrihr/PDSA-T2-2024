# def expanding(L):
#   for i in len(L):
#     abs(L[i] - L[i+1]) < abs(L[i+1] - L[i+2])
#     return True
#   return False

def expanding(L):
  if len(L) < 2:
    return True

  diffs = []
  for i in range(1, len(L)):
    diffs.append(abs(L[i] - L[i - 1]))

  for i in range(1, len(diffs)):
    if diffs[i] <= diffs[i-1]:
      return False

  return True


L = eval(input())
print(expanding(L))
