import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def closest_pair(points):
    def closest_pair_rec(px, py):
        n = len(px)
        if n <= 3:
            return min(distance(px[i], px[j]) for i in range(n) for j in range(i+1, n))

        mid = n // 2
        midpoint = px[mid]
        left_x = px[:mid]
        right_x = px[mid:]

        left_y = [p for p in py if p[0] <= midpoint[0]]
        right_y = [p for p in py if p[0] > midpoint[0]]

        d_left = closest_pair_rec(left_x, left_y)
        d_right = closest_pair_rec(right_x, right_y)
        d = min(d_left, d_right)

        strip = [p for p in py if abs(p[0] - midpoint[0]) < d]
        strip_len = len(strip)

        for i in range(strip_len):
            for j in range(i+1, min(i+7, strip_len)):
                d = min(d, distance(strip[i], strip[j]))

        return d
    
    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])

    return closest_pair_rec(px, py)

# Read input
n = int(input())
flags = []
for _ in range(n):
    x, y = map(int, input().split())
    flags.append((x, y))

# Calculate and print the minimum distance
result = closest_pair(flags)
print(f"{result:.3f}")