import sys
import math

import numberUtils

def main(parameters):
   number = int(parameters[1])
   product = 1
   for i in range(1, number + 1):
      product = product * (i / numberUtils.gcd(product, i))

   print(int(product))
      

if __name__ == '__main__':
   main(sys.argv)
