from math import ceil, sqrt



primes = []
i = 1
while (len(primes) < 10):
	isPrime = True
	for prime in primes:
		if (i%prime == 0):
			isPrime = False
			break
	if (isPrime):
		primes.append(i)
	i += 2
print primes