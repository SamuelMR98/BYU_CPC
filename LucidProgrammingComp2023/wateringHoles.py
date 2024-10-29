# Watering Holes

# You are running a park with several watering holes. Your job is to track which dinosaurs are at each watering hole, and report which ones are still there at the end of the day.

# Every time a dinosaur moves to a new watering hole or leaves the park, they register their movement with you. Each watering hole is identified by a positive integer.

# Input Format:

# The input will consist of a positive integer n, indicating the number of logs. Next will follow n lines. Each line will be 1 of the following 2 formats:

# timmytrex 2, meaning the dinosaur named timmytrex moved to watering hole 2.
# timmytrex 0, meaning the dinosaur named timmytrex left the park.

# Constraints: 

# Each dinosaur has a unique name
# Each dinosaur name consists of only lowercase letters
# Every watering hole will appear in at least 1 log
# There will be at most 1000 watering holes
# There will be at most 10,000 logs

# Output Format:

# Your output should be the list of dinosaurs left at each watering hole at the end of the day. The watering holes should be sorted in ascending numerical order. The dinosaurs at each watering hole should be printed as a space separated list in ascending alphabetical order. If no dinosaurs are left at a given watering hole, output n/a.

# Sample Input 0: 
# 5
# timmytrex 1
# allyallosaurus 1
# timmytrex 3
# allyallosaurus 0
# bobbybrontosaurus 3

# Sample Output 0:
# 1 n/a
# 3 bobbybrontosaurus timmytrex

# Sample Input 1:
# 9
# allyallosaurus 5
# pennypterodactyl 3
# rickyraptor 4
# allyallosaurus 1
# allyallosaurus 2
# rickyraptor 5
# igoriguanodon 5
# allyallosaurus 1
# igoriguanodon 1

# Sample Output 1:
# 1 allyallosaurus igoriguanodon
# 2 n/a
# 3 pennypterodactyl
# 4 n/a
# 5 rickyraptor

# solution:

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read input
n = int(input())

# Create a dictionary to store the dinosaurs at each watering hole
dinos = {}

# Iterate through each log

watering_holes = set()
for _ in range(n):
    # Read the log
    dino, hole = input().split()

    # Add the watering hole to the set
    if hole != "0":
        watering_holes.add(hole)

    # Update the dictionary
    if hole == "0":
        # The dinosaur left the park 
        if dino in dinos:
            del dinos[dino]
    else:
        # The dinosaur moved to a new watering hole
        dinos[dino] = hole

# dinos left at each watering hole at the end of the day (sorted in ascending numerical order)
# The dinosaurs at each watering hole should be printed as a space separated list in ascending alphabetical order. If no dinosaurs are left at a given watering hole, output n/a.

# print(dinos)
# print(watering_holes)

# find dinos in the same watering hole
dinos_in_same_hole = {}
for dino in dinos:
    hole = dinos[dino]
    if hole not in dinos_in_same_hole:
        dinos_in_same_hole[hole] = [dino]
    else:
        dinos_in_same_hole[hole].append(dino)

# print(dinos_in_same_hole)


# print the dinosaurs left at each watering hole at the end of the day

for hole in sorted(watering_holes):
    if hole in dinos_in_same_hole:
        print(hole, " ".join(sorted(dinos_in_same_hole[hole])))
    else:
        print(hole, "n/a")



