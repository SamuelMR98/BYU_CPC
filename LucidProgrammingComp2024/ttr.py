#!/usr/bin/env python3
# Trampoline Triumph

def find_optimal_strategy(times):
    effort_penalties = {75: 0.16, 80: 0.125, 85: 0.088, 90: 0.055, 95: 0.026, 100: 0.0}
    fatigue_penalties = {75: 0.015, 80: 0.022, 85: 0.032, 90: 0.045, 95: 0.060, 100: 0.1}
    efforts = [75, 80, 85, 90, 95, 100]

    best_time = float('inf')
    best_efforts = None

    def dfs(stroke, current_time, current_fatigue, current_efforts):
        nonlocal best_time, best_efforts
        
        if stroke == 4:
            if current_time < best_time:
                best_time = current_time
                best_efforts = current_efforts
            return

        for effort in efforts:
            time = times[stroke] * (1 + effort_penalties[effort]) * (1 + current_fatigue)
            new_fatigue = current_fatigue + fatigue_penalties[effort]
            new_time = current_time + time
            
            if new_time < best_time:
                dfs(stroke + 1, new_time, new_fatigue, current_efforts + [effort])

    dfs(0, 0, 0, [])
    return best_efforts, round(best_time, 1)

# Read input
n = int(input())
swimmers = [list(map(float, input().split())) for _ in range(n)]

# Process each swimmer
for swimmer in swimmers:
    efforts, time = find_optimal_strategy(swimmer)
    print(*efforts, f"{time:.1f}")