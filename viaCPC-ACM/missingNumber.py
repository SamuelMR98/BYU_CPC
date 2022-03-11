c = int(input())
l = int(input())

l = [int(a) for a in str(l)]

#find missing number in string
for i in range(1, c+1):
    if i not in l:
        print(i)
        break

