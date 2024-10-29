# T-Rex divvy up their hunting grounds into rectangular plots each day. The map of the hunting grounds is
# an N by N grid. Each grid cell is assigned a hunting value and the hunting value of a plot is the sum of the cells it covers. Rexy is hungry after escaping the shattered plains and wants to get a good plot. He will ask you for the total hunting value of many different rectangular plots.
# Rexy will give you the (y,x) coordinates of the top left and bottom right corners of the rectangle he is interested in. He chose the order y then x because in most dinosaur programming languages you index a 2D array as grid[y][x]. The coordinates are inclusive and 1 indexed. The origin, (1 , 1), is in the top left.

# Input:

# The first line of input will have two integers, N and Q, the dimension of the  NxN hunting grounds grid and the number of queries Terry will give you.
# The next N lines will esch have N separated integers, G_ij, This is the hunting grind
# The newx Q lines will each have 4 space separated integers y1, x1, y2, x2. These are the coordinates of the top left and bottom right corners of the rectangle Terry is interested in.

# Output:
# Q lines. Each lines should have the sum total hunting value of the rectangle of the grid

# Constraints:
# 1 <= N <= 1000
# 1 <= Q <= 10^5
# 0 <= G_ij <= 1000
# 1 <= y1 <= y2 <= N
# 1 <= x1 <= x2 <= N

# run time: max 10 seconds


# Sample Input 0:
# 6 3
# 6 1 3 4 5 2
# 2 3 1 1 1 1
# 4 7 2 1 9 3
# 0 1 0 9 2 3
# 9 9 7 9 9 3
# 2 3 2 7 8 1
# 2 2 3 4
# 1 1 1 1
# 3 5 6 6

# Sample Output 0:
# 15
# 6
# 38

# Sample Input 1:
# 1 1
# 7
# 1 1 1 1

# Sample Output 1:
# 7

# Sample Input 2:

# 4 6
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 1 1 2 3
# 1 2 2 3
# 1 1 1 4
# 4 4 4 4
# 1 4 4 4
# 1 1 4 4

# Sample Output 2:
# 24
# 18
# 10
# 16
# 40
# 136

# Solution:

import sys

# Read the first line of input
N, Q = map(int, input().split())

# Read the grid
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

# Read the queries and print the sum of the grid
queries = []
for _ in range(Q):
    y1, x1, y2, x2 = map(int, input().split())
    print(sum([sum(row[x1-1:x2]) for row in grid[y1-1:y2]]))


# Optimized Solution:

# Read the first line of input
N, Q = map(int, input().split())

# Read the grid
grid = [list(map(int, input().split())) for _ in range(N)]

# Calculate the cumulative sum for each row
cumulative_sum = [[0] * (N + 1) for _ in range(N)]
for i in range(N):
    for j in range(N):
        cumulative_sum[i][j + 1] = cumulative_sum[i][j] + grid[i][j]

# Read the queries and print the sum of the grid
for _ in range(Q):
    y1, x1, y2, x2 = map(int, input().split())
    total = 0
    for i in range(y1 - 1, y2):
        total += cumulative_sum[i][x2] - cumulative_sum[i][x1 - 1]
    print(total)


# ------------------------------

# Read the first line of input
N, Q = map(int, input().split())

# Read the grid
grid = [list(map(int, input().split())) for _ in range(N)]

# Calculate the cumulative sum for each row
cumulative_sum = [[0] * (N + 1) for _ in range(N)]
for i in range(N):
    for j in range(N):
        cumulative_sum[i][j + 1] = cumulative_sum[i][j] + grid[i][j]

# Read the queries and print the sum of the grid
for _ in range(Q):
    y1, x1, y2, x2 = map(int, input().split())
    total = 0
    for i in range(y1 - 1, y2):
        total += cumulative_sum[i][x2] - cumulative_sum[i][x1 - 1]
    print(total)
