# IQ Test

def next_number(l,n):
    """
    Return the next number in the sequence of integers that is
    generated by the number n.
    """
    for i in range(len(l)):
        if l[i] == n:
            return l[i+1]
    return l[0] + (n-1)*d
    

n = int(input())

l = []


for i in range(n):
    l.append(list(input().split()))

for i in range(n):
    lambda_ = int(l[i][0])

print(l)