# Tai's Formula
from traceback import print_tb


def trapezoidArea(t1, t2, v1, v2):
    return ((t2 - t1) * (v1 + v2) / 2)/1000


n = int(input())

l = []

area = 0

for i in range(n):
    l.append(list(map(float, input().split())))

for i in range(n):
    if i+1 < n:
        area += trapezoidArea(float(l[i][0]), float(l[i+1][0]), float(l[i][1]), float(l[i+1][1]))
print(area)