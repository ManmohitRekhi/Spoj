a = int(raw_input())
while a:
	b = raw_input().split()
	t = [c[::-1] for c in b]
	l = sum(map(int, t))
	while l%10 == 0:
		l /= 10
	l = str(l)
	print l[::-1]
	a -= 1
