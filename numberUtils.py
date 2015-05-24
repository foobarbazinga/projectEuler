import sys
import math

def gcd(a, b):
   # print('gcd:', a, b)
   if a < b:
      temp = a
      a = b
      b = temp
   remainder = math.floor(a % b)
   if remainder == 0:
      return b
   return gcd(b, remainder)

def primeFactors(number, primes):
   factors = set()
   while number != 1:
      for p in primes:
         if number % p == 0:
            factors.add(p)
            number = int(number / p)
            break
      else:
         factors.add(number)
         break
   return factors

def primeFactorization(number):
   maxPrimeFactor = math.floor(math.sqrt(number))
   primes = primesLowerThan(maxPrimeFactor + 1)
   factors = {}
   while number != 1:
      for p in primes:
         if number % p == 0:
            if p not in factors:
               factors[p] = 1
            else:
               factors[p] += 1
            number = int(number / p)
            break
      else:
         factors[number] = 1
         break
   return factors
         

# return list of all the primes up to primeCeiling, inclusive
def primesLowerThan(primeCeiling):
   numbers = [True for i in range(0, primeCeiling)]
   maxCheckValue = math.floor(math.sqrt(primeCeiling))

   numbers[0] = False
   numbers[1] = False
   for primeNdx in range(2, maxCheckValue + 1):
      if numbers[primeNdx] == True:
         for index in range(2 * primeNdx, primeCeiling, primeNdx):
            numbers[index] = False
   return set(ndx for ndx, val in enumerate(numbers) if val == True)

def generatePrimes(numPrimes):
   pass

def sieve(primeCeiling):
   numbers = [True for i in range(0, primeCeiling + 1)]
   maxCheckValue = math.floor(math.sqrt(primeCeiling))

   numbers[0] = False
   numbers[1] = False
   for primeNdx in range(2, maxCheckValue + 1):
      if numbers[primeNdx] == True:
         for index in range(2 * primeNdx, primeCeiling + 1, primeNdx):
            numbers[index] = False
   return [ndx for ndx, val in enumerate(numbers) if val == True]

