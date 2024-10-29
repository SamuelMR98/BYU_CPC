# Triceratops Evolution

# Triceratops are occasionally mistaken for predators, given their large horns and sturdy build. However, they are in reality herbivores who have evolved to gain various defensive traits. These traits are critical for the survival of the triceratops, as its relatively low speed prevents it from using escape as a means of deterring predators.

# Given the importance of these traits in the survival of the triceratops, we are interested in the probability that certain traits get passed on to future generations of triceratops. You are given three probabilities p_0, p_1, p_2 
#  denoting the odds of a child (generation i) inheriting the trait, given that zero, one, or two parents (generation i - 1) 
# have the trait respectively. Given the probability g1 that any given triceratops of generation 0 has the trait, determine the probability that any given triceratops of generation N will have the trait.

# Input Format

# The input format consists of one integer N, and four probabilities g_1, p_0, p_1, p_2, each on a separate line.
# We want to know the probability that any given triceratops of generation N has the trait.
# g_1 is the probability that any triceratops of generation 0 has the trait.
# p_0, p_1, p_2 are  the probabilities that a triceratops of the next generation inherits the trait, given zero, one, or two of its parents had the trait respectively.

# <N> <g_1> <p_0> <p_1> <p_2>

# Constraints:

# The target generation N will always be integer values between 1 and 9 inclusive.
# The probabilities g_1, p_0, p_1, p_2 will always be floating point values between 0.0 and 1.0 inclusive. (four decimal places of precision)
# ehrn a triceratops of generation i is born, it must have two parents of generation i - 1.

# Output Format

# Output the probability that any given triceratops of generation  N has the trait. our answer must differ by no more than 10^-3  from the exact solution.

# <probability>

# Sample Input 0
# 1 0.5 0.0 0.25 1.0

# Sample Output 0
# 0.3750

# Sample Input 1
# 1 0.2 0.25 0.5 1.0

# Sample Output 1
# 0.3600

# Sample Input 2
# 2 0.9 0.1 0.25 0.5

# Sample Output 2
# 0.2556

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# solution:

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read input

N, g1, p0, p1, p2 = map(float, input().split())
N = int(N)

def triceratops_evolution(N, g1, p0, p1, p2):
    # Initialize the probability of having the trait
    p = g1

    # Iterate through the generations
    for i in range(N):
        # Calculate the probability of having the trait in the next generation
        p = p * (p0 * (1 - p0) + 2 * p1 * (1 - p1) + p2 * (1 - p2))

    return p   

print(triceratops_evolution(N, g1, p0, p1, p2))







