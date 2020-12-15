"""
Student: Sarel Alush
ID: 316373851
Assignment no. 4
Program: triangle.py
"""



def main():
      height = int(input("Enter height: "))
      dollars = int(input("Enter number of $: "))
      spaces = int(input("Enter number of spaces: "))
      cnt_dollars = dollars  #counter to know how much $ print              
      cnt_spaces = 0 #counter to know how much space print
      if height <2: #check if the triangle small than 2
            print("Wrong input please try again :D !")
            return #stop the program
      for i in range(0,height): #run all rows
            for j in range(i,height): #run colums
                  print(" ",end="") #print height-i spaces 
            print("*" , end="")#print only one *
            for j in range(0,i*2-1):#run colums again
                  if i == height-1 : #for colum number one we need only one *
                        print("*",end="")
                  else: # The other situations that need to be in either $ or space
                        if cnt_dollars: #check if counter of $ true
                              print("$",end="") #print $
                              cnt_dollars-=1 #Subtract from counter of dollar 1
                              cnt_spaces = cnt_dollars == 0 and spaces or 0 #If the dollar counter is zero we move to spaces
                        else: 
                              print(" ",end="") # print space
                              cnt_spaces -=1 #Subtract from counter of space 1
                              cnt_dollars = cnt_spaces ==0 and dollars or 0 #If the spaces counter is zero we move to dollars
                                                      
                  if(j == i*2-2): #this for all right side rectangle and for the bottom of rectangle
                        print("*",end="")
                  
            print()#new line
main()
