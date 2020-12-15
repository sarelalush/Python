"""
Student: Sarel Alush
ID: 316373851
Assignment no. 1
Program: 1.py
"""

#string reverse
def reverse(s):
      if len(s)==0: #if list is null return
            return
      reverse(s[1:])
      print(s[0],end="")

#appeard func
def number_appeard(s,ch):
      num = 0
      if len(s)==0: #if list is null return
            return 0
      if s[0]==ch: #if found num++
            num = 1
      return num + number_appeard(s[1:],ch)#return num + others..

#check for same string
def same_string(s1,s2):
      if len(s1)==0 or len(s2)==0:#if equal in last check
            return True
      if len(s1) > len(s2) or len(s1) < len(s2) or s1[0] != s2[0]: #if len of string s1 big than s2 or else
            return False
      return same_string(s1[1:],s2[1:]) #check next locat


def main():
      s1 = input("please enter string to reverse :")
      reverse(s1)
      print()
      s2 = input("please enter string to check char appeard:")
      c = input("please enter char to check char appeard::")
      print(number_appeard(s1,c))
      s1 = input("please enter string1 :")
      s2 = input("please enter string 2 :")
      if(same_string(s1,s2)):
            print("equals")
      else:
            print("not equals")
      
main()
