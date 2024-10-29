# input positive integer n (size of the array)
# followed by the pivot values in the order they appear in the array
# example: 5 4 5 1 2 3

# get input



# output m = the number of values in the arry that could have served as pivot values to partition the array
m = 0

pivot = []

for i in range(n):
    left = arr[:i]
    right = arr[i+1:]
    if len(left) == 0:
        left = [0]
    if len(right) == 0:
        right = [0]
    if max(left) < arr[i] and min(right) > arr[i]:
        m += 1
        pivot.append(arr[i])

print(m, pivot)