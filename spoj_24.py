a = int(raw_input())
while a:
	t = int(raw_input())
	l = 1
	for i in range(1,t+1):
		l *= i
	print l
	a -= 1
