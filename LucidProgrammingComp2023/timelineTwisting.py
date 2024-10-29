# Timeline Twisting

# While popular media has shown certain species of dinosaurs as having lived during the same time period, in many cases these representations aren't accurate. For a variety of reasons (e.g., evolution, climate, ecology), the duration of time that certain species existed must be entirely before or entirely after some other species.

# You have a list of dinosaur species, the duration of time that each species is known to have existed, and any number of logical constraints on when a species could have existed relative to another species. Between two
# species A and B, there are two possible constraints:

# A lived before B
# A lived after B

# Determine the shortest length of time necessary such that all the dinosaur species could have existed in a logically consistent way

# Input Format:

# The first line:
# N = the amount of dinosaur species
# C = the amount of constraints

# The second line:
# N space separated integers. Call this sequence of numbers D, D_i is the duration of time that species i is known to have existed

# The next C lines:
# x y z
# x = the first species
# y = the second species
# z = the constraint (either x and y)

# Constraints:
 
# 1 <= N <= 10^3
# 0 <= C <= N * (N-1)
# 1 <= D_i <= 10^6
# 0 <= x,y < n
# z E set({1,2})
# There will always be at least one logically consistent way for all the dinosaur species to have existed

# Output Format:
# A single integer: the minimum amount of time required for all the species to have existed in a logically consistent way.

# Sample Input 0:
# 2 1
# 9 5
# 0 1 1

# Sample Output 0:
# 14

# Sample Input 1:
# 3 1
# 3 10 5
# 0 2 1

# Sample Output 1:
# 10

# Sample Input 2:
# 3 2
# 5 3 3
# 2 1 2
# 0 2 1

# Sample Output 2:
# 8

# solution:

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    queue = []

    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)

    sorted_order = []
    while queue:
        node = queue.pop(0)
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

def calculate_min_time(N, D, constraints):
    graph_before = defaultdict(list)
    graph_after = defaultdict(list)

    for x, y, z in constraints:
        if z == 1:
            graph_before[y].append(x)
            graph_after[x].append(y)
        else:
            graph_before[x].append(y)
            graph_after[y].append(x)

    sorted_before = topological_sort(graph_before)
    sorted_after = topological_sort(graph_after)

    min_time = 0
    min_before_time = [0] * N
    min_after_time = [float('inf')] * N

    for node in sorted_before:
        min_time = max(min_time, min_before_time[node] + D[node])
        min_before_time[node] = min_time

    for node in reversed(sorted_after):
        min_time = max(min_time, min_after_time[node] + D[node])
        min_after_time[node] = min_time

    return min_time

# Read input
N, C = map(int, input().split())
D = list(map(int, input().split()))
constraints = [list(map(int, input().split())) for _ in range(C)]

# Calculate and print the minimum time required
min_time = calculate_min_time(N, D, constraints)
print(min_time)
