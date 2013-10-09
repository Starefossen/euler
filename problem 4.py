ans = 0;
for i in range(999, 100, -1):
	for ii in range(999, 100, -1):
		sum = i*ii
		if (str(sum) == str(sum)[::-1]):
			#print sum
			if (sum > ans):
				ans = sum
		if (sum < ans):
			break
				
print ans