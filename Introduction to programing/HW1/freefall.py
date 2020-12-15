"""
Student: Sarel Alush
ID: 316373851
Assignment no. 1
Program: freefall.py
"""
import math



def main():
      G = 9.8
      height = input("Please enter the height : ")
      x = (2*int(height)) / G
      t = math.sqrt(x)
      v = G * t
      print("The time it takes for the stone to reach the floor is - ",t)
      print("damage speed is : ",v)
main()
