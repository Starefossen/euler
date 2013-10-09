sum = 0;
sqr = 0;
for i in range(1, 101):
	sqr += i*i
	sum += i
print ((sum*sum)-sqr)