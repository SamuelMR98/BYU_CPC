i = input().split()
l = int(i[0])
r = int(i[1])

if (l == 0 and r == 0):
    print("Not a moose")
elif (l == r and l != 0 and r != 0):
    print("Even", l+r)
else:
    print("Odd", max(l, r)*2)