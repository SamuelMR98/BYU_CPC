# Asteroid Escape

# N = number of locations 
# M = number of edges 
# F = amount of food to survive the journey
# Location 1 = starting location
# Location N = hihg point in which the dinosaur must reach

# Each location has a food count F_1 - F_N
# Given pairs of locations (i,j) you can only travel from i to j

# Determine the shortest path from location 1 to location N for the dinosaur such that it collects at least F food

# Input:
# N M F

# N space-separated integers F_1 - F_N

# M lines of two space-separated integers i j

# Output: 
# Print the lengh of the shortest path with at least F food

# Constraints:
# The number of locations N is between 2 <= N <= 250 
# The number of edges M is between 1 <= M <= 1500 
# The amount of food required F is between 0 <= F <= 5000
# The food at each location  F_1 - F_N is between 0 <= F_i <= 100
# If an edge goes from location  to location , it cannot be used to travel from  to 
# Any edge from a location  must go to some location  such that 
# No edge appears more than once
# There will always be at least one path from location  to location  that collects  food

# Sample Input:
# 3 2 6
# 3 1 3
# 1 2
# 2 3

# Sample Output:
# 2


# Sample Input 1:
# 5 5 10
# 1 2 3 4 0
# 1 2
# 2 3
# 3 4
# 3 5
# 4 5

# Sample Output 1:
# 4

# Sample Input 2:
# 4 6 8
# 4 4 20 3
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4

# Sample Output 2:
# 2

# ------------------------------

# Solution:

# ------------------------------

import sys
import math
from collections import deque

# Read input
N, M, F = map(int, input().split())

# Read the food counts
food_counts = list(map(int, input().split()))

# Read the edges
edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))

# Build the graph
graph = {}
for i in range(1, N + 1):
    graph[i] = []
for edge in edges:
    graph[edge[0]].append(edge[1])

# Perform a BFS

# Initialize the queue
queue = deque()
queue.append((1, food_counts[0]))

# Initialize the visited set
visited = set()
visited.add((1, food_counts[0]))

# Initialize the minimum distance
min_distance = math.inf

# Perform the BFS

while queue:
    current_node, current_food = queue.popleft()
    if current_node == N and current_food >= F:
        min_distance = min(min_distance, len(visited))
    for neighbor in graph[current_node]:
        if (neighbor, current_food + food_counts[neighbor - 1]) not in visited:
            queue.append((neighbor, current_food + food_counts[neighbor - 1]))
            visited.add((neighbor, current_food + food_counts[neighbor - 1]))

# Print the minimum distance
print(min_distance)
