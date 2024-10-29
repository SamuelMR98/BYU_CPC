#!/usr/bin/env python3
# Belly Flop Bonanza

import math

def parse_input(input_data):
    lines = input_data.strip().split('\n')
    n = int(lines[0])
    entries = []
    for line in lines[1:n+1]:
        name, coords, diameter = line.split(';')
        x, y = map(float, coords.strip()[1:-1].split(','))
        diameter = float(diameter)
        entries.append((name.strip(), (x, y), diameter))
    return entries

def calculate_effective_distance(entries):
    distances = []
    for name, (x, y), diameter in entries:
        center_distance = math.sqrt(x**2 + y**2)
        effective_distance = center_distance + (diameter / 2)
        distances.append((name, effective_distance))
    return distances

def get_top_three(distances):
    sorted_distances = sorted(distances, key=lambda x: x[1], reverse=True)

    return sorted_distances[:3]

def print_podium(podium):
    for name, _ in podium:
        print(name)

# Read input

input_data = []
while True:
    try:
        line = input()
        input_data.append(line)
    except EOFError:
        break

entries = parse_input('\n'.join(input_data))
distances = calculate_effective_distance(entries)
podium = get_top_three(distances)
print_podium(podium)