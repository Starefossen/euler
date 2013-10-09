fin = 0
small = 20
while (fin == 0):
	for i in range(20, 0, -1):
		if (small%i != 0):
			break
		if (i == 1):
			print small
			fin = 1
	small +=20