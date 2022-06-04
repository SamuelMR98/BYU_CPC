n = int(input())

l = []

for i in range(n):
    l.append(int(input()))

javelin = sum(l) - (n-1)

print(javelin)