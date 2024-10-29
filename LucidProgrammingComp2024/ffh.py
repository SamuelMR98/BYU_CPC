#!/usr/bin/env python3
# Fatigued Four Hundred

def calculate_optimal_effort_levels(swimmers):
    effort_level_penalties = {
        75: 0.16, 80: 0.125, 85: 0.088, 90: 0.055, 95: 0.026, 100: 0.0
    }
    progressive_fatigue_penalties = {
        75: 0.015, 80: 0.022, 85: 0.032, 90: 0.045, 95: 0.060, 100: 0.1
    }
    effort_levels = [75, 80, 85, 90, 95, 100]

    results = []

    for times in swimmers:
        best_time = float('inf')
        best_efforts = None

        for e1 in effort_levels:
            time1 = times[0] * (1 + effort_level_penalties[e1])
            fatigue1 = progressive_fatigue_penalties[e1]
            
            for e2 in effort_levels:
                time2 = times[1] * (1 + effort_level_penalties[e2]) * (1 + fatigue1)
                fatigue2 = fatigue1 + progressive_fatigue_penalties[e2]
                
                for e3 in effort_levels:
                    time3 = times[2] * (1 + effort_level_penalties[e3]) * (1 + fatigue2)
                    fatigue3 = fatigue2 + progressive_fatigue_penalties[e3]
                    
                    for e4 in effort_levels:
                        time4 = times[3] * (1 + effort_level_penalties[e4]) * (1 + fatigue3)
                        total_time = time1 + time2 + time3 + time4

                        if total_time < best_time:
                            best_time = total_time
                            best_efforts = (e1, e2, e3, e4)

        results.append((best_efforts, round(best_time, 1)))

    return results

# Read input
n = int(input())
swimmers = [list(map(float, input().split())) for _ in range(n)]

# Calculate optimal effort levels and predicted times
results = calculate_optimal_effort_levels(swimmers)

# Print results
for efforts, time in results:
    print(f"{efforts[0]} {efforts[1]} {efforts[2]} {efforts[3]} {time:.1f}")