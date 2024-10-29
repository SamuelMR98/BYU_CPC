#!/usr/bin/env python3
# Bullseye Bonus

# Fenwick Tree implementation for range updates and point queries
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    
    def query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total

def solve_archery_competition(n, m, initial_scores, bullseye_events):
    # Initialize Fenwick Trees for sum and count
    sum_tree = FenwickTree(n)
    count_tree = FenwickTree(n)
    
    # Initialize Fenwick Trees with initial scores
    for i, score in enumerate(initial_scores, 1):
        sum_tree.update(i, score)
        count_tree.update(i, 1)
    
    # Process bullseye events
    for x, y, l, r in bullseye_events:
        sum_range = sum_tree.query(r) - sum_tree.query(l - 1)
        count_range = count_tree.query(r) - count_tree.query(l - 1)
        k = sum_range // count_range
        
        sum_tree.update(x, k)
        sum_tree.update(y, -k)
    
    # Find the winner
    max_score = float('-inf')
    winner = 0
    for i in range(1, n + 1):
        score = sum_tree.query(i) - sum_tree.query(i - 1)
        if score > max_score:
            max_score = score
            winner = i
    
    return winner

# Read input
n, m = map(int, input().split())
initial_scores = list(map(int, input().split()))
bullseye_events = [list(map(int, input().split())) for _ in range(m)]

# Solve and print the result
result = solve_archery_competition(n, m, initial_scores, bullseye_events)
print(result)