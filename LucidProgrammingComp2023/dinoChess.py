# Dino Chess

# It has been a few hundred years but the chess developers have decided to finally update the game by adding a new piece, the dino. The dino can move similarly to the king in eight directions but unlike the king it moves
# M squares (but no less than M squares) and can jump over other pieces. 
# (When a dino moves each position must change by either +M , -M , or 0  but both position changes can not be 0.)

# With the addition of the new piece folks have started thinking about how this piece will interact with the board and the question of what is the maximum amount of non-attacking dinos that can be placed on an 
# N x N board is asked. A non-attacking dino is one such that none of the squares it attacks are occupied by another dino.

# Given a dino that can move M squares on an N x N board board, what is the maximum amount of non-attacking dinos that can be placed on a single board?

# Input Format

# The first (and only) line will contain two space-separated numbers.

# M = integer denoting the number of squares the dino can move

# N = integer denoting the size of the board

# Constraints:

# 1 < M <= N <= 1000
# M and N are integers

# Output Format
# Your output should be a single integer denoting the maximum amount of non-attacking dinos you can place on an N by N board.

# Sample Input 0
# 2 5

# Sample Output 0
# 9

# Sample Input 1
# 3 12

# Sample Output 1
# 36

# Sample Input 2
# 2 2

# Sample Output 2
# 4

# Solution:

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read input
M, N = map(int, input().split())

def max_non_attacking_dinos(M, N):
    if M <= 0 or N <= 0:
        return 0

    # Calculate the maximum number of dinos in one row
    max_in_row = (N - M) // M + 1

    # Calculate the maximum number of dinos in one column
    max_in_col = (N - M) // M + 1

    # Calculate the maximum number of non-attacking dinos
    max_dinos = max_in_row * max_in_col

    return max_dinos

print(max_non_attacking_dinos(M, N))