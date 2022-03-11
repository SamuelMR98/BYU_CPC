i = input().split()
n = int(i[0])
m = int(i[1])

c = (n + m) / 2
d = abs(n - m) / 2 

start = c+1 - d
end = c+1 + d
if (m + n) % 2 != 0:
    end += 1

for i in range(int(start), int(end) + 1):
    print(i)

