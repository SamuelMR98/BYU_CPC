#!/usr/bin/env python3
# Dance Competition

from collections import defaultdict

# Rolling hash function uses Rabin-Karp algorithm
def rolling_hashes(moves, N):
    if len(moves) < N:
        return set()
    
    hash_set = set()
    
    for i in range(len(moves) - N + 1):
        sub_seq = tuple(moves[i:i+N])
        hash_set.add(hash(sub_seq))
    
    return hash_set

def count_copying_dancers(D, N, dancers):
    hash_to_dancers = defaultdict(set)
    copying_dancers = set()
    
    for name, moves in dancers:
        dancer_hashes = rolling_hashes(moves, N)
        for h in dancer_hashes:
            if h in hash_to_dancers:
                copying_dancers.update(hash_to_dancers[h])
                copying_dancers.add(name)
            hash_to_dancers[h].add(name)
    
    return len(copying_dancers)

# Read input
D, N = map(int, input().split())
dancers = []
for _ in range(D):
    line = input().split()
    name, moves = line[0], line[1:]
    dancers.append((name, moves))

# Compute and print result
result = count_copying_dancers(D, N, dancers)
print(result)