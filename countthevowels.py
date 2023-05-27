vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

s = input()

count = 0

for i in s:
    if i in vowels:
        count += 1

print(count)