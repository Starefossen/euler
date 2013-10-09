import time
s = time.time()

def numDivisors(n):
	c = 0
	for i in range(1, n+1):
		if (n%i == 0):
			c += 1
			print i, n/i
			
		#if (c > 500):
			#return c
	#print c
	return c	

sum, i = 0, 1
while i < 100:
	sum += i
	
	print "TRIANGLE", sum
	d = numDivisors(sum)
	print "SUM =", d
	
	#if (sum > 500):
		
		#break
	i += 1
	
#print sum

print time.time() - s