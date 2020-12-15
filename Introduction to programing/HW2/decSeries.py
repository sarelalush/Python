"""
Student: Sarel Alush
ID: 316373851
Assignment no. 2
Program: decSeries.py
"""

N = 10

def main():
      number = 0
      cnt = 1
      bigSeries = 0
      lastNumber = 0
      for i in range(0,N):
            number = int(input("Enter Number : "))
            if(number < lastNumber and i != 0): #check if number small than last number
                  cnt+=1 #inc counter
            elif (number > lastNumber): #check if number big than last number
                  cnt = 1 #Reset counter
            if(cnt > bigSeries): #check if counter bigger than bigseries
                  bigSeries = cnt #Now we have found a new series

            lastNumber = number
      print("bigSeries is : ",bigSeries)
main()
