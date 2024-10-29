#!/usr/bin/env python3
# Penguin Slide

# Read input
n = int(input())
penguin_times = []

for _ in range(n):
    line = input()
    name, time = line.rsplit(' - ', 1)
    penguin_times.append((name, int(time)))

# Sort penguins based on their times in ascending order
penguin_times.sort(key=lambda x: x[1])

# Extract the top three penguins
top_three = penguin_times[:3]

# Format and print the output
positions = ["First", "Second", "Third"]
for i, (name, _) in enumerate(top_three):
    print(f"{positions[i]}: {name}")