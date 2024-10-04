def is_prime(n):
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True


# print(is_prime(8))
# print(is_prime(7))


def Twin_Primes(n, m):
  n = max(2, n)
  twins = []
  for i in range(n, m+1):
    # if i + 2 > m:
    #   break
    if i + 2 <= m and is_prime(i) and is_prime(i+2):
      twins.append((i, i+2))
  return twins


n = int(input())
m = int(input())
print(Twin_Primes(n, m))
