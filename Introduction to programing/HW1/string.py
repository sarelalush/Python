"""
Student: Sarel Alush
ID: 316373851
Assignment no. 3
Program: string.py
"""


def main():
      name = input("Enter your name: ")
      for ch in name:
            if ch == " ":
                  print(end="\n")
            else:
                  print(ch,end="")
main()
