# Territory Dispute

# Dinosaurs may be territorial, but that doesn't mean they can't be civilized. The dinosaur council is having problems assigning territory to its members, and it needs your help to make the final decision as to which pieces of land will be given out individually and which pieces will be made public by the council.

# The dinosaurs have compiled a list of potential territories to give out, noting the total size of each. You have been enlisted to find the grouping of territories that will cause the least strife between all of the dinosaurs while still leaving enough public land to be enjoyed by everyone.

# In other words, you need to find one territory for each dino such that the difference between the smallest and largest territories handed out is minimized while keeping the sum of the unused territories at least as large as the required size.

# Input Format:

# The first line of input will contain three space separated integers:

# N: the number of pieces of land
# D: the number of dinosaurs that need territory
# S: the minimum size of land that must be left over for the council

# The remaining lines of input will each contain a single integer representing the size of a piece of land.

# Constraints:
# 0 < N <= 10^6
# 0 < D <= N
# 0 <= S <= 10^9

# The total size of land will never exceed 2 x 10^9

# The problem will always have at least one solution that gives every dinosaur land and leaves enough left over for the council.

# Output Format:

# A single integer: the minimum difference between the smallest and largest territories handed out while still meeting the requirement for left over land.

# Sample Input 0: 

# 5 3 1
# 2
# 3
# 2
# 7
# 5

# Sample Output 0:

# 1

# Sample Input 1:

# 5 4 10
# 10
# 9
# 8
# 7
# 4

# Sample Output 1:

# 5

# solution:

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read input
N, D, S = map(int, input().split())

# Read the territories
territories = []
for _ in range(N):
    territories.append(int(input()))

def min_difference(N, D, S, territories):
    # Sort the territories
    territories.sort()

    # Calculate the total size of the territories
    total_size = sum(territories)

    # Calculate the minimum size of a territory
    min_size = total_size // D

    # Calculate the maximum size of a territory
    max_size = territories[-1]

    # Calculate the minimum difference
    min_difference = max_size - min_size

    return min_difference

print(min_difference(N, D, S, territories))