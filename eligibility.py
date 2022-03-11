n = input()
for i in range(int(n)):
    z = input().split()
    name = z[0]
    school = int(z[1][:4])
    if school >= 2010:
        print(name, "eligible")
        continue
    
    birthdate = int(z[2][:4])
    if birthdate >= 1991:
        print(name, "eligible")
        continue
    
    courses = int(z[3])
    if courses >= 41:
        print(name, "ineligible")
        continue
    print(name, "coach petitions")
