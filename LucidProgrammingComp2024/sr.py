#!/usr/bin/env python3
# Sailboat Regatta

from collections import deque

def minimum_time_to_hole(width, length, cooldown, winds):
    queue = deque()
    visited = set()

    # Initialize the queue with starting positions
    for x in range(width):
        queue.append((-1, x, 0, 1, 0))  # (y, x, vx, vy, cooldown)
        visited.add((-1, x, 0, 1, 0))

    time_steps = 0

    while queue:
        for _ in range(len(queue)):
            y, x, vx, vy, cd = queue.popleft()

            # Move the boat
            new_y, new_x = y + vy, x + vx

            # Check if we've reached or passed the finish line
            if new_y >= length:
                return time_steps

            # Check if we're out of bounds
            if new_x < 0 or new_x >= width:
                continue

            # Apply wind effect if we're on the course
            if 0 <= new_y < length:
                wind_x, wind_y = winds[new_y][new_x]
                new_vx, new_vy = vx + wind_x, vy + wind_y
            else:
                new_vx, new_vy = vx, vy

            # Generate next states
            if cd == 0:
                # Try both raising and lowering sails
                queue.append((new_y, new_x, new_vx, new_vy, cooldown))  # Raise sails
                queue.append((new_y, new_x, vx, vy, cooldown))  # Lower sails
                visited.add((new_y, new_x, new_vx, new_vy, cooldown))
                visited.add((new_y, new_x, vx, vy, cooldown))
            else:
                # Maintain current sail state
                queue.append((new_y, new_x, vx, vy, cd - 1))
                visited.add((new_y, new_x, vx, vy, cd - 1))

        time_steps += 1

    return -1  # Cannot finish within bounds

# Read input
width, length, cooldown = map(int, input().split())
winds = []
for _ in range(length):
    row = [tuple(map(int, coord.strip('()').split(','))) for coord in input().split()]
    winds.append(row)

# Calculate and print result
result = minimum_time_to_hole(width, length, cooldown, winds)
print(result)