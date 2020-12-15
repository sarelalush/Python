"""
Student: Sarel Alush
ID: 316373851
Assignment no. 1
Program: stats.py
"""

#get string and return list
def string_to_list(numbers):
      return numbers.split()

#return the average of all numbers in list
def average(numbers):
      sum_numbers = 0
      cnt=0
      for num in numbers:
            sum_numbers = sum_numbers + int(num) #sum of all numbers
            cnt = cnt + 1
      return sum_numbers / cnt #sum / The number of numbers

#return the big number in list
def large_number(numbers):
      return max(numbers)

#return the position of big number in list
def pos_large_number(numbers):
      return numbers.index(max(numbers))
	  
#return the small number in list     
def pos_small_number(numbers):
      return numbers.index(min(numbers))
	  
#return the position of small number in list      
def small_number(numbers):
      return min(numbers)

#check if the series is rising
def check_rising_series(numbers):
      for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                  return False
      return True

#check if the series is go down
def check_down_series(numbers):
      for i in range(len(numbers)-1):
            if numbers[i] < numbers[i+1]:
                  return False
      return True

#print the type of series (we have 3 states)
def check_type_of_series(numbers):
      if check_rising_series(numbers):
            return "Rising"
      elif check_down_series(numbers):
            return "Goes down"
      else:
            return "not rising and not goes down"
			
def main():
      numbers_list = string_to_list(input("Please enter numbers : "))
      print("the average of numbers is :" , average(numbers_list))
      print("The biggest number is {0} and its pos is {1}".format(large_number(numbers_list),pos_large_number(numbers_list)))
      print("The smallest number is {0} and its pos is {1}".format(small_number(numbers_list),pos_small_number(numbers_list)))
      print("the type of series is :",check_type_of_series(numbers_list))
main()
