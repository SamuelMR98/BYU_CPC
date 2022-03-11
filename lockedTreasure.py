class COMBINATIONS:
    MEM = {}
    def coeficient(n,k):
        if n == k or k == 0:
            return 1
        if (n,k) not in COMBINATIONS.MEM:
             COMBINATIONS.MEM[(n,k)] = COMBINATIONS.coeficient(n-1,k) + COMBINATIONS.coeficient(n-1,k-1)
        return COMBINATIONS.MEM[(n,k)]

for _ in range(int(input())):
    y,z = map(int,input().split())
    print(COMBINATIONS.coeficient(y,z-1))
