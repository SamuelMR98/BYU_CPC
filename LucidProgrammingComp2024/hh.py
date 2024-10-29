#!/usr/bin/env python3
# Heartfelt Hanging

def maximize_training_sessions(available_sessions, num_athletes, training_times, score_improvements):
    # Create a DP array to store the maximum score improvements for each session capacity
    dp = [0] * (available_sessions + 1)

    for i in range(num_athletes):
        time = training_times[i]
        improvement = score_improvements[i]

        # We need to iterate backwards to prevent overwriting results of the current iteration
        for j in range(available_sessions, time - 1, -1):
            dp[j] = max(dp[j], dp[j - time] + improvement)

    return dp[available_sessions]

# Read input
available_sessions = int(input())
num_athletes = int(input())
training_times = list(map(int, input().split()))
score_improvements = list(map(int, input().split()))

# Calculate and print the maximum score improvements
max_improvements = maximize_training_sessions(available_sessions, num_athletes, training_times, score_improvements)
print(max_improvements)