import sys
tests = int(sys.stdin.readline())
for _ in range(tests):
	l = sys.stdin.readline().split(' ')
	l[:]=map(float,l)
	r=l[0]
	b=l[1]
	m=l[2]
	r /= 100
	s = b
	for i in range(1200):
		interest = round(sum * r * 100+ 0.05) / 100
		s += interest
		s -= m
		if(s < 0.0001):
			break
	if(sum < 0.0001):
		print(i+1)
	else:
		print("impossible")
