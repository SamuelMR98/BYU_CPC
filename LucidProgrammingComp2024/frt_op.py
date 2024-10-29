#!/usr/bin/env python3
# Fastest Relay Team (Optimized)

def min_swimming_time(n, times):
    # Initialize the DP array with infinity
    dp = [float('inf')] * (1 << 4)
    dp[0] = 0  # Base case: no strokes selected, zero time

    for i in range(n):
        for mask in range(1 << 4):
            for j in range(4):
                if (mask & (1 << j)) == 0:  # If j-th stroke is not used
                    new_mask = mask | (1 << j)
                    dp[new_mask] = min(dp[new_mask], dp[mask] + times[i][j])

    return dp[(1 << 4) - 1]  # Return the time for all strokes used

# Read input
n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
result = min_swimming_time(n, times)
print(result)