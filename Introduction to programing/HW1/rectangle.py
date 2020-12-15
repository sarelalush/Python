"""
Student: Sarel Alush
ID: 316373851
Assignment no. 2
Program: rectangle.py
"""


def main():
      length = int(input("Please enter the length of rectangle:"))
      ch = input("Please enter a character: ")
      for i in range(4):
            for j in range(length):
                  if i == 0 or i == 3 or j == 0 or j == length-1:
                        print(ch,end='')
                  else:
                        print(" ",end="")
            print()      
main()
