# T-Rex Pushups

# Bob, the T-Rex, is tired of skipping upper body day. He'd like to do more pushups. One problem: he's got a big head and little arms. Bob has never been one to give up though, so he's devised a plan to get gains. He knows a place that has a lot of holes in the ground from some recent meteor strikes. He can do pushups by these holes because his head can fit in them and his arms can actually touch the ground. His head is 4 ft long, so each hole needs to be at least 4 ft deep. Unfortunately, Bob is self-conscious, so he never wants to go to the same hole twice.

# The terrain is given as an array of integers, where terrain[i] is the elevation in ft at index i. Bob needs at least a 4 ft difference between elevations. Additionally, Bob only ever faces forward when doing pushups, so terrain[i] - terrain[i+1] >= 4. (-4 would not count)

# How many places does Bob have to do pushups?

# Input Format:

# <N>
# <H_1> <H_2> ... <H_N>

# N is the length of the terrain array

# Constraints:
# 0 < n <= 10^4
# 0 <= H_i <= 10^4

# Output Format:

# Output an integer which represents the number of place Bob can do pushups (as defined above)

# Sample Input 0:

# 5
# 1 2 3 4 5

# Sample Output 0:

# 0

# Sample Input 1:
# 10
# 10 6 2 6 10 6 1 0 10 0

# Sample Output 1:
# 5

# Solution:

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read input
N = int(input())
terrain = list(map(int, input().split()))

# print(N)
# print(terrain)

# Find the number of places Bob can do pushups
count = 0
for i in range(N-1):
    if terrain[i] - terrain[i+1] >= 4:
        count += 1
print(count)
