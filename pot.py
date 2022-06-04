# Pot
# N is the number of addends from the task
# The following N lines contains the integer Pi from the task

N = int(input())

l = []
s = 0

for i in range(N):
    l.append(input())

for i in range(N):
    t = l[i]
    s += int(t[0:-1]) ** int(t[-1])

print(s)