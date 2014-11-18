n = int(raw_input())
while n:
	a = int(raw_input())
	sum = 0
	count = 5
	while a / count > 0:
		sum += a/count
		count *= 5
	print sum
	n -= 1 