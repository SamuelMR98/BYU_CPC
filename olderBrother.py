#Older Brother
# Finite Fields
# q = p^k prime power
# p = prime number
# k >= 1    

import math

def isPrime(n):
    if n == 2:
        return True
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



n = int(input())
found = False

if (n==1):
    print("no")
    found = True
elif isPrime(n):
    print("yes")
    found = True
else:
    for i in range(2,int(math.sqrt(n))+1):
        if isPrime(i):
            val = i
            j = 2
            while (val < n):
                val = i**j
                j+=1
            if val == n:
                print("yes")
                found = True
                break
if not found:
    print("no")