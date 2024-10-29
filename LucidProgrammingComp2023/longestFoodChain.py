# Longest Food Chain

# Many dinosaurs survive by eating other dinosaurs, in this problem we want to determine the longest chain of dinosaurs from herbivore to apex predator.

# Input:

# N
# A <- B,C
# D <- F
# ...
# {predator} <- {list of preys separated by ","}

# N = number of dinosaurs

# Constraints:
# 0 < N <= 100
# inputs will not have cycles

# Output:
# Print the length of the longest chain

# Sample Input 0:
# 3
# A <- B,C
# B <- C
# C <- D

# Sample Output 0:
# 3

# Sample Input 1:
# 12
# A <- B
# B <- C
# C <- D
# D <- E
# E <- F
# F <- G
# G <- H
# H <- I
# I <- J
# J <- K
# K <- L
# L <- M 

# Sample Output 1:
# 13

# Solution:

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read input
N = int(input())

# Read the food chain
foodChain = {}
for _ in range(N):
    prey, predators = input().split("<-")
    foodChain[prey.strip()] = [pred.strip() for pred in predators.split(",")]

# print(foodChain)

# For each dinosaur, compute the longest chain

def longestChain(dinosaur):
    if dinosaur not in foodChain:
        return 0
    else:
        return 1 + max([longestChain(pred) for pred in foodChain[dinosaur]])
    
print(max([longestChain(dinosaur) for dinosaur in foodChain.keys()]) + 1)

# ------------------------------
N = int(input())

relationships = []
for _ in range(N):
    relationships.append(input())

def longest_food_chain(N, relationships):
    # Create a dictionary to represent the relationships between dinosaurs
    graph = {}
    for line in relationships:
        predator, preys = line.split(" <- ")
        preys = preys.split(',')
        graph[predator] = preys

    def dfs(dinosaur):
        if dinosaur not in graph:
            return 0
        max_chain_length = 0
        for prey in graph[dinosaur]:
            max_chain_length = max(max_chain_length, 1 + dfs(prey))
        return max_chain_length

    max_chain_length = 0
    for dinosaur in graph:
        max_chain_length = max(max_chain_length, dfs(dinosaur))

    return max_chain_length + 1  # Add 1 for the apex predator

print(longest_food_chain(N, relationships))
