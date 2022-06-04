# Pawn Shop
# Subset

N = int(input())
O = input().split()
R = input().split()

final = []
lo = 0
hi = 1

d = dict()
d2 = dict()
while hi <= N:
    i = O[hi - 1]
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

    i = R[hi - 1]
    if i in d2:
        d2[i] += 1
    else:
        d2[i] = 1

    if d == d2:
        to_print = R[lo: hi]
        print(' '.join(to_print), end='')
        if hi != N:
            print(" # ", end='')
        lo = hi
        d = dict()
        d2 = dict()

    hi += 1
print()