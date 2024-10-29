# Fossil Fuel

# You are babysitting and dino nuggets are for dinner! The kids are jealous though and will only eat if they all get the same amount of food. Given the number of kids to feed and a list of the sizes of the dino nuggets left in the bag, determine the maximum amount you can feed the kids such that they all eat the same amount.

# Input Format
# The first line will contain an integer K, the number of kids to be fed
# The second line will be a space separated list of integers N that denotes the size of each dino nugget available to serve the kids

# <K>
# <N_0> <N_1> ... <N_M>

# Constraints:

# All kids must eat the same amount of food, not necessarily the same number of nuggets though. For example, one nugget of size 2 is the same amount of food as two nuggets of size 1.
# Nuggets cannot be split into pieces. For example, a nugget of size 3 cannot be split into a nugget of size 2 and another nugget of size 1.
# Not all nuggets have to be used.
# The number of kids to feed K <= 10
# Nugget sizes N_i <= 20
# The lenght of the list of nuggets sizes M <= 30

# Output Format
# Your output should be the maximum amount of food you can feed each kid. If there is no way to evenly divide the nuggets among all the kids, your output should be 0.

# Sample Input 0
# 2
# 1 3 8 2 4

# Sample Output 0
# 9

# Sample Input 1
# 4
# 1 1 5 1 7 2 3 2 1 1 4

# Sample Output 1
# 7

# Sample Input 2

# 3
# 1 1 5 1 2 3 4 1 9

# Sample Output 2
# 9

# solution:

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read input
K = int(input())
nugget_sizes = list(map(int, input().split()))

nugget_sizes.sort(reverse=True)

def divide_nuggets(total, k):
    return total % k == 0

def find_max_nuggets(kids, nuggets):
    total_nuggets = sum(nuggets)
    
    for i in range(len(nuggets)):
        if divide_nuggets(total_nuggets, kids):
            return total_nuggets // kids
        total_nuggets -= nuggets[i]
    
    # If you can't evenly divide, return 0
    return 0

# Calculate and print the result
max_food = find_max_nuggets(K, nugget_sizes)
print(max_food)
