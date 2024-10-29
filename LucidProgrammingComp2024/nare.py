#!/usr/bin/env python3
# New Air Rifle Event

from typing import List, Tuple

def orientation(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]) -> int:
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def is_convex_hull(points: List[Tuple[int, int]]) -> bool:
    n = len(points)
    if n < 3:
        return False
    
    # Check if all points are collinear
    if all(orientation(points[0], points[1], points[i]) == 0 for i in range(2, n)):
        return False
    
    # Find the orientation of the first three points
    last_orientation = orientation(points[-1], points[0], points[1])
    
    for i in range(n):
        current_orientation = orientation(points[i], points[(i+1) % n], points[(i+2) % n])
        if current_orientation == 0:  # Collinear points
            return False
        if (last_orientation > 0 and current_orientation < 0) or (last_orientation < 0 and current_orientation > 0):
            return False
        last_orientation = current_orientation
    
    return True

def point_in_polygon(point: Tuple[int, int], polygon: List[Tuple[int, int]]) -> bool:
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if point[1] > min(p1y, p2y):
            if point[1] <= max(p1y, p2y):
                if point[0] <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (point[1] - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or point[0] <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def distance_squared(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def solve_air_rifle_challenge(A: int, N: int, M: int, competitors: List[Tuple[str, List[Tuple[int, int]]]]) -> List[str]:
    successful_competitors = []
    
    for name, shots in competitors:
        if len(set(shots)) != N:  # Check for duplicate shots
            continue
        
        convex_hull_points = shots[:N-1]
        last_shot = shots[-1]
        
        if not is_convex_hull(convex_hull_points):
            continue
        
        if not (point_in_polygon(last_shot, convex_hull_points) or last_shot in convex_hull_points):
            continue
        
        if distance_squared(last_shot, (0, 0)) > M*M:
            continue
        
        successful_competitors.append(name)
    
    return successful_competitors

# Read input
A, N, M = map(int, input().split())
competitors = []
for _ in range(A):
    line = input().split()
    name = line[0]
    shots = [tuple(map(int, coord.split(','))) for coord in line[1:]]
    competitors.append((name, shots))

# Solve and print results
results = solve_air_rifle_challenge(A, N, M, competitors)
for name in results:
    print(name)