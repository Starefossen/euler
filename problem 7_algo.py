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
			
p = primes(2, 100000000)

c = 0
for k in p:
	if p[k]:
		c+=1
		
print c

print time.time() - s