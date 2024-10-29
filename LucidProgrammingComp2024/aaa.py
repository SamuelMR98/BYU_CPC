#!/usr/bin/env python3
# Athlete Area Allocation

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def min_distance(flags):
    min_d = float('inf')
    for i in range(len(flags)):
        for j in range(i+1, len(flags)):
            d = distance(int(flags[i][0]), int(flags[i][1]), int(flags[j][0]), int(flags[j][1]))
            if d < min_d:
                min_d = d
    # roung to 3 decimal places
    #min_d = round(min_d, 3)
    return min_d

#Input
n = int(input()) # number of flags
flags = [] # list of flags
for i in range(n):
    flags.append(input().split())


# Output the minimum distance
result = min_distance(flags)
print(f"{result:.3f}")


def test_min_distance():
    # Sample Input 0
    input0 = [(0, 0), (1, 1)]
    expected0 = 1.414
    result0 = min_distance(input0)
    assert abs(result0 - expected0) < 0.001, f"Test 0 failed: Expected {expected0}, got {result0:.3f}"

    # Sample Input 1
    input1 = [(4, 5), (1, 1), (2, 6), (1, 4), (6, 3)]
    expected1 = 2.236
    result1 = min_distance(input1)
    assert abs(result1 - expected1) < 0.001, f"Test 1 failed: Expected {expected1}, got {result1:.3f}"

    print("All tests passed.")

# Run the tests
test_min_distance()