import sys
import primeUtils

def main(parameters):
   # generate all primes below 2 million
   primes = primeUtils.sieve(1999999)
   print('sum of primes below 2 million:', sum(primes))

main(sys.argv)
