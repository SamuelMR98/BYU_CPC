# Odd Echo
# Receive N number of words and print the odd ones.

N = int(input())

for i in range(1,N+1):
    if i % 2 != 0:
        print(input())
    else:
        input()
    