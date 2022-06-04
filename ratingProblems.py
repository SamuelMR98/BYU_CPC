# Rating Problems
# n = total number of judges
# k = number of judges who have rated each problem

i = input().split()
n = int(i[0])
k = int(i[1])

ratings = []

for i in range(k):
    ratings.append(int(input()))

print(sum(ratings, (n-k)*-3) / n, sum(ratings, (n-k)*3) / n, sep=' ')

