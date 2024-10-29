# Museum Analytics  

# In the historic city of South Jordan, an extraordinary abundance of dinosaur fossils paved the way for the inception of the illustrious Prehistoric Relics Museum. This newfound treasure trove drew global tourists eager to marvel at the exquisite remains. As the newly appointed Museum registrar, your pivotal role now centers around the quest to unveil the visitors' most beloved dinosaur. Thus, you embarked on a survey, inviting patrons to submit their cherished dinosaur choices. The survey results are elegantly presented: one response per line, with each response listing dinosaurs separated by commas. Now, the challenge awaits: can you identify the dinosaur that truly captivates the most hearts? (Note: It is guaranteed that there will be no ties.)

# The first line contains the number of response N. Each of the next N lines contain a list of dinosaur names of arbitrary size, separated by comma ,. Note: The dinosaur names may contain lowercase and uppercase letters, spaces, and hyphens.

# N
# <dinosaur 1> , <dinosaur 2> , ... , <dinosaur X>
# <dinosaur 1> , <dinosaur 2> , ... , <dinosaur Y>
# ...
# <dinosaur 1> , <dinosaur 2> , ... , <dinosaur Z>

# Constraints:

# it is guaranteed that there will be just one most beloved dinosaur (no ties)
# It is guaranteed the list of beloved dinosaurs submitted by the visitors is valid, i.e., it does not contain any duplicates.
# 1 <= N <= 10^4
# 1 <= N <= 10^4
# 1 <= |total number of dinosaus submiteed by each visitor| <= 10
# <= |total number of unique dinosaurs| <= 10^4
# 5 <= |the length of the name of a dinosaur| <= 25

# Output Format:

# On the first line, print the name of the most beloved dinosaur. On the second line, print the number of people it is beloved for, i.e., the number of votes.

# <most beloved dinosaur>
# <number of people it is beloved for>

# Sample Input 0:
# 2
# San Juanosaurus
# South Jordan Swiftclaw,San Juanosaurus,Saltlakosaurus,Provopteryx

# Sample Output 0:
# San Juanosaurus
# 2

# Sample Input 1:
# 4
# Juab Canyonwhirl,South Jordan Swiftclaw,Saltlakosaurus,Provopteryx
# Provopteryx,Redrockraptor,San Juanosaurus
# Wasatchceratops
# Vermilionvelociraptor,San Juanosaurus,Provopteryx,Wasatchceratops

# Sample Output 1:
# Provopteryx
# 3

# Sample Input 2:
# 5
# Provopteryx,Vermilionvelociraptor,Utahraptorix
# Utahraptorix,Wasatchceratops,San Juanosaurus,Escalantespin
# South Jordan Swiftclaw,Redrockraptor,Saltlakosaurus,Wasatchceratops
# Wasatchceratops,South Jordan Swiftclaw,Utahraptorix
# Escalantespin,Utahraptorix

# Sample Output 2:
# Utahraptorix
# 4

# Solution:
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read input
N = int(input())

# Read the votes
votes = {}
for _ in range(N):
    for dinosaur in input().split(","):
        if dinosaur not in votes:
            votes[dinosaur] = 1
        else:
            votes[dinosaur] += 1

# Find the most beloved dinosaur
maxVotes = 0
mostBeloved = ""
for dinosaur in votes:
    if votes[dinosaur] > maxVotes:
        maxVotes = votes[dinosaur]
        mostBeloved = dinosaur

# Print the most beloved dinosaur
print(mostBeloved)
print(maxVotes)
