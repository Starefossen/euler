import time, math
s = time.time()

# a < b < c
# a*a + b*b = c*c

def triplet(sum = 1000):
	for a in range(1, sum/2):
		for b in range(a+1, sum/2):
			c = math.sqrt(a**2+b**2)
			if(c%1 == 0 and a+b+c == sum):
				return '%i < %i < %i = %i' % (a, b, c, int(a*b*c))

print triplet(1000)

print time.time() - s