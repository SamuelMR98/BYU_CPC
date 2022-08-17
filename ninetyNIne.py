from ast import While


n = 1
print(n)

while True:
    n = int(input())
    if n > 98:
        break
    n += min(3 - n % 3, 2)

    print(n)
    if n == 99:
        break
