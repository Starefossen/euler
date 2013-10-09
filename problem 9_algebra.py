import time, math
s = time.time()

#I simplified with algebra before programming:

#Using Euclid's formula:
#a=(m^2-n^2)
#b=(2mn)
#c=(m^2+n^2)

#if a+b+c = 1000 then
#m(2m+2n)=1000
#and
#n=(1000-2m^2)/2m

#m must be greater than n, which only occurs if m > 15
#the product will always be greater than 1000 if m >22

for m in range(15,22):
	n = (1000-2*m*m)/(2*m)
	a = (m*m-n*n)
	b = (2*m*n)
	c = (m*m + n*n)
	if(a*a+b*b == c*c):
		if(a+b+c == 1000):
			print a*b*c
			
print time.time() - s