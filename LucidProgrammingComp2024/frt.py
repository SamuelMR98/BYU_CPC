#!/usr/bin/env python3
# Fastest Relay Team

from itertools import permutations

def min_swimming_time(n, times):
    min_time = float('inf')
    
    for perm in permutations(range(n), 4):
        total_time = sum(times[perm[i]][i] for i in range(4))
        min_time = min(min_time, total_time)
    
    return min_time

# Read input
n = int(input())
swimmer_times = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
result = min_swimming_time(n, swimmer_times)
print(result)