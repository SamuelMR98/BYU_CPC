
def num_of_paymets(l):
    
    return None 




n = int(input())
l = []

for i in range(n):
    z = list(float(x) for x in input().split())
    l.append(z)

for i in range(n):
    print(num_of_paymets(l[i]))