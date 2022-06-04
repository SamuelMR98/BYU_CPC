# Social Distancing
# S = number of seats at the table
# N = number of people already seated
# List of where N pople are seated

l = input().split()
S = int(l[0])
N = int(l[1])

m = input().split()


max_people = S % 2

seats_occupied = []
for i in range(N):
    seats_occupied.append(int(m[i]))
    if int(m[i]) + 1 < S:
        seats_occupied.append(int(m[i]) + 1)
    if int(m[i]) - 1 > 0:
        seats_occupied.append(int(m[i]) - 1)
    if int(m[i]) - 1 < 0:
        seats_occupied.append(S)
    if int(m[i]) + 1 == S:
        seats_occupied.append(1)
    

if (S%2 == 0):
    print(S - len(seats_occupied))
else:
    print((S-1) - len(seats_occupied))




