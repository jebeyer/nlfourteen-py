#!/user/bin/python

from itertools import combinations
import numpy

# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primesfrom2to(n):
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

# get list of primes less than n
primes = primesfrom2to(3400)

# find numbers satisfying:
# i) number is the composite of two primes
# ii) digit sum of the number is equal to the difference of its prime factors

mynums = []
for (a,b) in combinations(primes,2):
    abprod = a * b
    abdiff = b - a
    dsum = sum(int(digit) for digit in str(abprod))
    if abdiff == dsum:
        mynums.append(abprod)
        #print(abprod,a,b,sep=', ')
        
# sort the list and print to screen
mynums.sort()
print(mynums)

