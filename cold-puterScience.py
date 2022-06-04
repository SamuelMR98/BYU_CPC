# Cold-puter Science
# Given N number of temperatures
# Output the number that are less than 0

N = int(input())
l = input().split()

counter = 0

for i in l:
    if int(i) < 0:
        counter += 1

print(counter)