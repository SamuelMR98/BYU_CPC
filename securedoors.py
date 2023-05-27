log = set()

n = int(input())

for i in range(n):
    output = ""
    activity = input().split()
    if activity[0] == "entry":
        if activity[1] in log:
            output = activity[1] + " entered (ANOMALY)"
        else:
            output = activity[1] + " entered"
            log.add(activity[1])
    else:
        if activity[1] in log:
            output = activity[1] + " exited"
            log.remove(activity[1])
        else:
            output = activity[1] + " exited (ANOMALY)"
    print(output)
        

