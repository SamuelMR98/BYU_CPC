
# The input is one line and specifies the problems that Hneitir needs to solve
#The problems are numbered from 1 up to 1000 and are listed in ascending order, separated by semicolons (;). If two or more problems are in a row, that range is specified with -.

s = str(input())

s = s.split(';')

c = 0

for i in range(len(s)):
    s[i] = s[i].split('-')
for i in range(len(s)):
    if len(s[i]) == 1:
        c+=1
    else:
        c += (int(s[i][1]) - int(s[i][0]) + 1)
        
print(c)