#!/usr/bin/env python3
# Swimming Divisions

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.top_ranked = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            self.top_ranked[px] = x
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.top_ranked[py] = x
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.top_ranked[px] = x
        else:
            self.parent[py] = px
            self.top_ranked[px] = x
            self.rank[px] += 1

def solve_swimming_competitions():
    n = int(input())
    competitors = [input().strip() for _ in range(n)]
    name_to_index = {name: i for i, name in enumerate(competitors)}
    
    uf = UnionFind(n)
    
    while True:
        event = input().strip()
        if event == 'END':
            break
        
        if event.startswith('COMPETITION'):
            m = int(event.split()[1])
            participants = [input().strip() for _ in range(m)]
            winner = name_to_index[participants[0]]
            for participant in participants[1:]:
                uf.union(winner, name_to_index[participant])
        
        elif event.startswith('REQUEST'):
            requester = name_to_index[event.split()[1]]
            division = uf.find(requester)
            top_ranked = uf.top_ranked[division]
            print(competitors[top_ranked])

# Run the solution
solve_swimming_competitions()