import sys
import math

import primeUtils

# find the largest prime factor of 600851475143

def main(parameters):
   if len(parameters) < 1:
      return
   
   number = int(parameters[1])
   maxFactor = math.floor(math.sqrt(number))
   primes = primeUtils.primesLowerThan(maxFactor + 1)
   factors = primeUtils.primeFactors(number, primes)
   print('Prime factors of', number, 'are', factors)
   print('Max prime factor is', max(factors))



if __name__ == '__main__':
   main(sys.argv)
