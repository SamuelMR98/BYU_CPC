# BYU CPC
#Teikein

print(sum(map(lambda z: (z[0] + 1) * z[1], enumerate(sorted([float(input().split()[1]) for i in range(int(input()))], reverse=True)))))