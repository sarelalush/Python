


def main():
      sentance = input("Please enter a sentence: ")
      words = 1
      for i in range(0,len(sentance)): #run all chars in "sentance"
            if sentance[i] == " ": #if this char equals to space 
                  print() #new line
                  words+=1 #counter words inc +1
            else:
                  print(sentance[i],end="") #print char
            
      print("\nThere are" ,words, "words in: " ,sentance)

main()
