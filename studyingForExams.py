l = input().split()
N = int(l[0])
T = int(l[1])

def grade(t, a, b, c):
    return float((a*t**2) + (b*t) + c)


def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg


list = []
for i in range(N):
    i = input().split()
    g = []
    g.append(float(i[0]))
    g.append(float(i[1]))
    g.append(float(i[2]))
    list.append(g)

ll = []
for i in range(N):
    ll.append(grade(T, list[i][0], list[i][1], list[i][2]))

print(cal_average(ll))