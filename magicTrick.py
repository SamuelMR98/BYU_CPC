import collections

s = input()

d = collections.defaultdict(int)

for c in s:
    d[c] += 1

print(d)
d2 = dict(sorted(d.items(), key=lambda item: item[1]))
sorted_dict = collections.OrderedDict(d2)
print(sorted_dict)