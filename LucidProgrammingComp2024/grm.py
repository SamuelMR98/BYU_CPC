#!/usr/bin/env python3
# Gymnastics Routine Maker

from collections import defaultdict

def parse_input():
    N = int(input())
    moves = {}
    preceding_moves = defaultdict(list)
    
    for _ in range(N):
        parts = input().split()
        move_name = parts[0]
        max_score = int(parts[1])
        percentage_confidence = int(parts[2])
        moves[move_name] = (max_score, percentage_confidence)
        for prev_move in parts[3:]:
            preceding_moves[move_name].append(prev_move)
    
    return moves, preceding_moves

# Dynamic programming solution using a 2D table
def max_expected_score(moves, preceding_moves):
    dp = defaultdict(lambda: defaultdict(float))
    
    for move, (max_score, confidence) in moves.items():
        if 'start' in preceding_moves[move]:
            dp[1][move] = max_score * confidence / 100

    for i in range(2, 11):
        for move, (max_score, confidence) in moves.items():
            expected_score = max_score * confidence / 100
            for prev_move in preceding_moves[move]:
                if prev_move != 'start':
                    dp[i][move] = max(dp[i][move], dp[i-1][prev_move] + expected_score)

    return max(dp[10].values()) / 10

# Get input
moves, preceding_moves = parse_input()
result = max_expected_score(moves, preceding_moves)
print(f"{result:.3f}")