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

# get a list of primes less than n
primes = primesfrom2to(100000000)

# find numbers satisfying:
# i) number is the composite of two primes
# ii) digit sum of the number is equal to the difference of its prime factors

mynums = []
ii = 0
lastprime = len(primes) - 1
while ii < lastprime:
    jj = ii + 1
    while jj < len(primes):
        abprod = primes[ii] * primes[jj]
        abdiff = primes[jj] - primes[ii]
        dsum = sum(int(digit) for digit in str(abprod))
        
        # if difference larger than possible digit sum, skip
        prodlen = len(str(abprod))
        maxdsum = (prodlen + 3) * 9
        if abdiff > maxdsum:
            break

        if abdiff == dsum:
            #print(abprod,primes[ii],primes[jj],sep=' ')
            mynums.append(abprod)

        jj += 1

    ii += 1
    
# sort the list and print to screen
mynums.sort()
for k in range(len(mynums)):
    print(k+1,mynums[k],sep=' ')

