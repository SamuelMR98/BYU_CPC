# Finding An A
# Single string that contains an "a"
# Output: the suffix of the string that contains the first "a"

s = input()

#find the first "a"
for i in range(len(s)):
    if s[i] == "a":
        print(s[i:])
        break
