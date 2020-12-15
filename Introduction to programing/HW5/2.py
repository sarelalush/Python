"""
Student: Sarel Alush
ID: 316373851
Assignment no. 1
Program: 2.py
"""

def myfunc(num):
      if num <= 1:#if num < 1 return ""
            return ""
      i = 0
      for i in range(2,num+1):#run from 2 to num 
            if num%i == 0:#if num % i is zero
                  break #stop
      return myfunc(num//i)+ str(i) +"*"#not get number you find and call to function for another

def main():
      s=myfunc(180)[:-1]#withut last char ... exam - 1*2*3*4* <--- last char
      print(s)
      
main()
