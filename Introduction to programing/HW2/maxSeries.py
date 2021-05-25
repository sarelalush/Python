

def main():
      number = 1
      average = 0
      cell_min = 0
      cell_max = 0
      i = 0
      number = int(input("Enter numbers, 0 to stop:"))
      max_num = number
      min_num = number
      while number != 0: #stop when user enter zero
            average += number #sum of all numbers
            if number > max_num: #if you have new big number
                  max_num = number
                  cell_max = i #get the loaction of new big
            if number < min_num: #if you have new small number
                  min_num = number
                  cell_min = i #get the loaction of new small
            i+=1 #to know how much numbers we have
            number = int(input("Enter numbers, 0 to stop:"))
      print("avarge - ",round(average/i, 2)) #print avarge
      print("max value is ",max_num ,"in cell",cell_max+1)#print Max and loaction
      print("min value is ",min_num, "in cell ",cell_min+1)#print Min and loaction

main()
