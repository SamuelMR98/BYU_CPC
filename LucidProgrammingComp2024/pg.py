#!/usr/bin/env python3
# Pinball Golf

from collections import defaultdict, deque

def parse_input():
    N, L = map(int, input().split())
    flippers = []
    for _ in range(N):
        x, y, k = map(int, input().split())
        displacements = list(map(int, input().split()))
        flippers.append(((x, y), displacements))
    return N, L, flippers

def probability_of_ball_reaching_hole(N, L, flippers):
    graph = defaultdict(list)
    for (x, y), displacements in flippers:
        for d in displacements:
            new_x, new_y = x + d, y - 1
            if new_y >= 0:
                graph[(x, y)].append((new_x, new_y))
            else:
                graph[(x, y)].append((0, 0))  # Hole position

    probabilities = defaultdict(float)
    probabilities[(0, L)] = 1.0
    queue = deque([(0, L)])
    visited = set()

    while queue:
        current_pos = queue.popleft()
        if current_pos in visited:
            continue
        visited.add(current_pos)

        current_prob = probabilities[current_pos]
        if current_pos == (0, 0):
            continue

        possible_moves = graph[current_pos]
        if not possible_moves:
            # If no flipper, ball continues straight down
            new_pos = (current_pos[0], max(0, current_pos[1] - 1))
            probabilities[new_pos] += current_prob
            if new_pos not in visited:
                queue.append(new_pos)
        else:
            prob_per_move = current_prob / len(possible_moves)
            for next_pos in possible_moves:
                probabilities[next_pos] += prob_per_move
                if next_pos not in visited:
                    queue.append(next_pos)

    return probabilities[(0, 0)]

# Main execution
N, L, flippers = parse_input()
probability = probability_of_ball_reaching_hole(N, L, flippers)
print(f"{probability:.6f}")