import string
from sys import stdin

from numpy import empty

def isJolly(a):
    diffSet = [False] * (len(a))
    for i in range(0, len(a)-1):
        d = abs(a[i] - a[i+1])
        if (d == 0 or d > len(a)-1 or diffSet[d] == True):
            return False
        diffSet[d] = True
    return True

l = []

for line in stdin:
    if line == '':
        break
    l.append(list(map(int, line.split())))

for i in range(len(l)):
    if isJolly(l[i]):
        print("Jolly")
    else:
        print("Not jolly")

