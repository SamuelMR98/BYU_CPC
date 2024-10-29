#!/usr/bin/env python3
# Tennis Training

def min_cost_for_training(days, costs):
    dp = [0] * (days[-1] + 1)
    days_set = set(days)
    
    for i in range(1, len(dp)):
        if i not in days_set:
            dp[i] = dp[i-1]
        else:
            dp[i] = min(
                dp[max(0, i-1)] + costs[0],
                dp[max(0, i-7)] + costs[1],
                dp[max(0, i-30)] + costs[2]
            )
    
    return dp[-1]

# Read input
days = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Calculate and print the result
result = min_cost_for_training(days, costs)
print(result)