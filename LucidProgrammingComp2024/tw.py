#!/usr/bin/env python3
# Tug of War

from itertools import permutations

# Calculate the number of winning arrangements
def calculate_winning_arrangements(N: int, P: float, D: list, M: list) -> int:
    count = 0
    
    # Generate all permutations of indices for pulling power
    for perm in permutations(range(N)):
        arrangement_power = sum(D[perm[i]] * M[i] for i in range(N))
        if arrangement_power > P:
            count += 1
    
    return count

# Read input
N, P = map(float, input().split())
N = int(N)
D = list(map(float, input().split()))
M = list(map(float, input().split()))

# Calculate and print the result
result = calculate_winning_arrangements(N, P, D, M)
print(result)