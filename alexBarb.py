# Alex and Barb
# k = cards on the table
# turns and take form m to n cards
# Alex begins

i = input().split()
k = int(i[0])
m = int(i[1])
n = int(i[2])

count = 1

while k > 1:
    if n <= k:
        k -= n
    else:
        if k in range(m, n):
            


    count += 1

if count % 2 == 0:
    print("Barb")
else:
    print("Alex")

