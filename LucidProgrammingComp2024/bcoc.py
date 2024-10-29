#!/usr/bin/env python3
# Bouncy Castle Obstacles Course

import heapq

def parse_input():
    num_nodes = int(input())
    nodes = [input().strip() for _ in range(num_nodes)]
    num_obstacles = int(input())
    graph = {node: [] for node in nodes}
    for _ in range(num_obstacles):
        a, b, time = input().split()
        time = int(time)
        graph[a].append((b, time))
        graph[b].append((a, time))
    return nodes, graph

# Dijkstra's algorithm
def fastest_route(nodes, graph):
    start, end = nodes[0], nodes[-1]
    pq = [(0, start)]  # (total_time, node)
    times = {node: float('inf') for node in nodes}
    times[start] = 0

    while pq:
        total_time, current = heapq.heappop(pq)
        
        if current == end:
            return total_time
        
        if total_time > times[current]:
            continue
        
        leak_effect = total_time // 10
        
        for neighbor, base_time in graph[current]:
            new_time = total_time + base_time + leak_effect
            if new_time < times[neighbor]:
                times[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))
    
    return -1  # No path found

# Read input
nodes, graph = parse_input()
result = fastest_route(nodes, graph)
print(result)