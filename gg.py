def convert(a):
    l = []
    while (a[1] != 1):
        l.append(a[0]/a[1])
        a = [a[1],a[0]%a[1]]
        l.append(a[0])
    return l

a = [28,5]
print(convert([28,5]))