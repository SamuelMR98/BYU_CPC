# Server

n = input().split()
z = input().split()

counter = 0
suma = 0
for i in range(int(n[0])):
    suma += int(z[i])
    if suma > int(n[1]):
        break
    counter += 1

print(counter)