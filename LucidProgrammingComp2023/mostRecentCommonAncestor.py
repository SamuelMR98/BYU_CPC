# Most Recent Common Ancestor

# Your colleagues at the Prehistoric Relics Museum are making an effort to group dinosaur exhibits by evolutionary relationships. As one of the paleontologists on call, they frequently ask you to consult your phylogenetic trees to figure out how closely related two different dinosaurs are. In the interest of saving time that you would rather devote to actual field work, you decide to write a program for them to compute most recent common ancestry.

# Input Format:

# <N>
# <Ancestor> -- <Descendant>
# ...
# <Ancestor> -- <Descendant>
# <First>
# <Second>

# The first line contains a single positive integer N. 
# The following N lines contain the names of two dinosaurs clades, separated bu spaces and "--", indicating that the second clade is a descendant of the first.

# Constraints:
# 1 <= N <= 1000
# The ancestry relationships given will form a single, rooted tree.
#   There are no cycles.
#   Every clade, expect for the root, will have exactly one ancestor. (No test case will have anastomosis.)
#   Any two clades, except for the root, will have exactly one most recent common ancestor in the tree.
# Neither of the two clades named at the end of the input will be an ancestor, direct or indirect, of the other.

# Output Format:

# Output a single line with the name of the clade that is the most recent common ancestor of the two dinosaurs named at the end of the input.
# A clade is a common ancestor if it is an ancestor of both clades named at the end of the input.
# A clade is the most recent common ancestor if is a common ancestor and also not an ancestor of any other common ancestor.


# Sample Input 0:
# 2
# dinosaurs -- avian dinosaurs
# dinosaurs -- non-avian dinosaurs
# avian dinosaurs
# non-avian dinosaurs

# Sample Output 0:
# dinosaurs

# Sample Input 1:
# 2
# Archosaurs -- Crocodiles
# Archosaurs -- Birds
# Birds
# Crocodiles

# Sample Output 1:
# Archosaurs

# Sample Input 2:
# 5
# Ornithoscelida -- Theropoda
# Dinosauria -- Sauropodomorpha
# Dinosauria -- Ornithoscelida
# Ornithoscelida -- Ornithischia
# Theropoda -- Aves
# Ornithischia
# Theropoda

# Sample Output 2:
# Ornithoscelida

# Solition:

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read input

N = int(input())

# Read the ancestry relationships
ancestry = {}
for _ in range(N):
    ancestor, descendant = input().split(" -- ")
    ancestry[descendant] = ancestor

# Read the two dinosaurs
first = input()
second = input()

# Find the ancestors of the first dinosaur
first_ancestors = set()
while first in ancestry:
    first = ancestry[first]
    first_ancestors.add(first)

# Find the ancestors of the second dinosaur
second_ancestors = set()
while second in ancestry:
    second = ancestry[second]
    second_ancestors.add(second)

# Find the most recent common ancestor
print(first_ancestors.intersection(second_ancestors).pop())

# ------------------------------

# optimized solution:
# Read input
N = int(input())

# Initialize a dictionary to represent the clades and their relationships
clade_tree = {}
for _ in range(N):
    ancestor, descendant = input().split(" -- ")
    clade_tree[descendant] = ancestor

# Read the two clades for which we want to find the most recent common ancestor
first_clade = input().strip()
second_clade = input().strip()

# Function to find the ancestors of a clade
def find_ancestors(clade):
    ancestors = set()
    while clade in clade_tree:
        clade = clade_tree[clade]
        ancestors.add(clade)
    return ancestors

# Find the ancestors of both clades
first_ancestors = find_ancestors(first_clade)
second_ancestors = find_ancestors(second_clade)

# Find the most recent common ancestor
common_ancestors = first_ancestors.intersection(second_ancestors)

# Determine the most recent common ancestor that is not an ancestor of any other common ancestor
for ancestor in sorted(common_ancestors):
    is_most_recent_common_ancestor = True
    for other_ancestor in common_ancestors - {ancestor}:
        if ancestor in find_ancestors(other_ancestor):
            is_most_recent_common_ancestor = False
            break
    if is_most_recent_common_ancestor:
        most_recent_common_ancestor = ancestor
        break

# Print the most recent common ancestor
print(most_recent_common_ancestor)

