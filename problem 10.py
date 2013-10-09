import time
s = time.time()

def primes(start, end):
	p = {}
	for i in range(start, end):
		p[i] = True
	
	i = start
	while(i*i < end):
		#print p[i]
		if (p[i]):
			j = 0
			k = (i*i)+(j*i)
			while (k < end):
				p[k] = False
				j += 1
				k = (i*i)+(j*i)
		i += 1
	
	return p
			
p = primes(2, 2000000)
print time.time() - s

s = time.time()
sum = 0
for k in p:
	if p[k]:
		sum += k
		
print sum

print time.time() - s