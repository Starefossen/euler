tmp = 1
f0 = 0
f1 = 1
count = 0;
while (f1 < 4000000):
	tmp = f0 + f1
	f0 = f1
	f1 = tmp
	#print f1
	if (f1%2 == 0):
		count = count + f1
print count