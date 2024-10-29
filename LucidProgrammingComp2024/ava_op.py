#!/usr/bin/env python3
# Athletes' Village Arrangement OP

def parse_input(input_lines):
    n = int(input_lines[0])
    preferences = {}
    for i in range(1, 2*n, 2):
        country = input_lines[i].strip()
        neighbors = set(input_lines[i+1].strip().split())
        preferences[country] = neighbors
    return preferences

# DFS with backtracking
def is_valid_arrangement(arrangement, preferences):
    n = len(arrangement)
    for i in range(n):
        left_neighbor = arrangement[i - 1]  # Previous country (circular)
        right_neighbor = arrangement[(i + 1) % n]  # Next country (circular)
        if left_neighbor not in preferences[arrangement[i]] or right_neighbor not in preferences[arrangement[i]]:
            return False
    return True

def can_form_ring(preferences):
    countries = list(preferences.keys())
    n = len(countries)

    def backtrack(arrangement):
        if len(arrangement) == n:
            return is_valid_arrangement(arrangement, preferences)
        
        for country in countries:
            if country not in arrangement:
                if not arrangement or country in preferences[arrangement[-1]]:
                    arrangement.append(country)
                    if backtrack(arrangement):
                        return True
                    arrangement.pop()
        return False

    return backtrack([])

# Read input
input_lines = []
while True:
    try:
        line = input()
        input_lines.append(line)
    except EOFError:
        break

# Parse input and check if a valid ring can be formed
preferences = parse_input(input_lines)
result = can_form_ring(preferences)

# Print the result
print(str(result).lower())