import sys
import math
import primeUtils

# we need the 10,001 prime number
def main(parameters):
   limit = 5000000 
   primes = primeUtils.sieve(limit)
   print('number of primes below', limit, ':', len(primes))
   
   print('10001st prime:', primes[10000])



main(sys.argv)
