"""
Student: Sarel Alush
ID: 316373851
Assignment no. 3
Program: dice3.py
"""
import random

def main():  
      n = int(input("Please enter n: "))
      k = int(input("Please enter k: "))
      cnt = 0
      my_iter = 0
      for i in range(0,n): #run 0 to N
            a = random.randint(1, 6) 
            b = random.randint(1, 6)
            c = random.randint(1, 6)
            print(a,b,c)
            if a == b and b == c and my_iter < k: #check if random numbers equals and my flag(my_iter) small than k 
                  my_iter = i+1 #inc my_iter
                  cnt +=1 #inc cnt to know how much "Reached" we have
                  
      if cnt < k : #lose game Because there is not enough "Reached"
            print("Sorry You Lose :(")
            print("Reached",cnt, "equal series after",i+1,"games")
      else:#win the game
            print("You Win :D")
            print("Reached",cnt, "equal series after",my_iter,"games")
            
      
main()
