#!/usr/bin/env python3
# Athletes' Village Arrangement

from itertools import permutations

def get_input(input_lines):
    n = int(input_lines[0]) # number of countries
    preferences = {}
    for i in range (1, 2*n, 2):
        country = input_lines[i].strip()
        preference = input_lines[i+1].strip().split()
        preferences[country] = preference
    #print(preferences)
    return preferences

def is_valid_ring(arrangement, preferences):
    n = len(arrangement)
    for i in range(n):
        left_neighbor = arrangement[i - 1]  # Previous country (circular)
        right_neighbor = arrangement[(i + 1) % n]  # Next country (circular)
        if left_neighbor not in preferences[arrangement[i]] or right_neighbor not in preferences[arrangement[i]]:
            return False
    return True

def can_form_ring(preferences):
    countries = list(preferences.keys())
    for arrangement in permutations(countries):
        if is_valid_ring(arrangement, preferences):
            return True
    return False

# Read input

input_lines = []
while True:
    try:
        line = input()
        input_lines.append(line)
    except EOFError:
        break

preferences = get_input(input_lines)
result = can_form_ring(preferences)

print(str(result).lower())