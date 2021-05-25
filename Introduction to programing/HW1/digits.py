


def main():
     num = input("Enter a 4-digit number: ")
     if len(num) != 4:
           print("Error ! Your number is illegal ...")
           return 0
     for i in range(6):
           for j in range(4):
                 if(i==0):
                       print(num[3-j],' ',end="")
                 elif(i>0 and i<5):
                       if(j==4-i):
                             print(num[j],end="")
                       else:
                             print("   ",end="")
                 else:
                       print(num[j]," ",end="") 
           print()
main()
