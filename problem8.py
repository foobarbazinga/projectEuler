import sys
import math
import operator
import functools

import numberUtils

def readDigitsFromFile(fileName):
   with open(fileName) as f:
      contents = f.read()
   
   return [int(c) for c in contents if c.isdigit()]

def findNumbersAndProduct(digits):
   if len(digits) < 13:
      return

   product = functools.reduce(operator.mul, digits[:13])
   largest = product

   for ndx in range(13, len(digits)):
      product /= digits # what about 0

def main(parameters):
   if len(parameters) < 2:
      return

   digits = readDigitsFromFile(parameters[1])
   print(digits)


if __name__ == '__main__':
   main(sys.argv)
