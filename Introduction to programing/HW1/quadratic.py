"""
Student: Sarel Alush
ID: 316373851
Assignment no. 5
Program: quadratic.py 
"""
import math

def main():
      a = int(input("Enter first parameter (a): "))
      b = int(input("Enter first parameter (b): "))
      c = int(input("Enter first parameter (c): "))
      if(b**2-4*a*c < 0):
            print("No Solutions!!")
            return 0      
      x1 =  (-b-(math.sqrt(b**2-4*a*c)))/2*a
      x2 =  (-b+(math.sqrt(b**2-4*a*c)))/2*a
      if(x1 == x2):
            print("one solutions: " ,x1)
      else:
            print("two solutions: " ,x1,x2)
main()
