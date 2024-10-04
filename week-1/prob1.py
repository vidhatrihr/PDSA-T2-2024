def check_for_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n** 0.5)+1):
        if n % i == 0:
            return False
    return True
    
# print(check_for_prime(1))
# print(check_for_prime(2))
# print(check_for_prime(6))
# print(check_for_prime(8))
    
def primeproduct(m):
        if m <= 0:
                return False
        for i in range(2, int(m ** 0.5)+1):
                if m % i == 0:
                    if check_for_prime(i) and check_for_prime(m//i):
                        return True
        return False

m = int(input())
print(primeproduct(m))
