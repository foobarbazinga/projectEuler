import sys
import math

# return list of all the primes up to primeCeiling, inclusive
def seive(primeCeiling):
   numbers = [True for i in range(0, primeCeiling + 1)]
   maxCheckValue = math.floor(math.sqrt(primeCeiling))

   numbers[0] = False
   numbers[1] = False
   for primeNdx in range(2, maxCheckValue + 1):
      if numbers[primeNdx] == True:
         for index in range(2 * primeNdx, primeCeiling + 1, primeNdx):
            numbers[index] = False
   return [ndx for ndx, val in enumerate(numbers) if val == True]

