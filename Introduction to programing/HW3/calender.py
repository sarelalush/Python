"""
Student: Sarel Alush
ID: 316373851
Assignment no. 2
Program: calender.py
"""

MONTH_NUMBER =['January','February','March','April','May','June','July','August','September','October','November','December'] #all the month list
DAYS = ['Su','Mo','Tu','We','Th','Fr','Sa'] #all days list

#get all days until a month we need this for first day in month
def get_all_days_until_month(month , year = 0):
	sum_of_days = 0
	for i in range(0,MONTH_NUMBER.index(month)):
		sum_of_days += get_days_in_month(MONTH_NUMBER[i],year)
	return sum_of_days

#get all days until a year we need this for first day in year
def get_all_days_until_year(year):
	sum_of_days = 2
	for i in range(year-1900):
		if check_leap_year(1900+i):
			sum_of_days+=366
		else:
			sum_of_days+=365
	return sum_of_days

#check if year is leap year or not
def check_leap_year(year):
	is_leap_year = False
	if (year % 4) == 0:  
		if (year % 100) != 0:  
			is_leap_year = True
	if (year % 400) == 0:
			is_leap_year = True
	return is_leap_year
	   
#here we get the first day in month!
def get_first_day_in_month(year,month):
	first_day = get_all_days_until_year(year) + get_all_days_until_month(month,year) #Connect the days up to that year with the days up to that month
	return first_day%7 #here we get the day after after we did his module operation for several days in week

#print the calender
def print_days_in_month(day,year,month):
	cnt = day == 0 and day+7 or day
	days = "".join(["{:<4}"] * len(DAYS)).format(*DAYS) #list have all days in row 1
	days += "\n" 
	for i in range(1,cnt):
		days+="{:<4}".format("") #Print earnings until the day the month begins
	for j in range(1,get_days_in_month(month,year)+1):
		days+="{:<4}".format(j)#print all days in month
		if(cnt%7==0): #new line after 7 print
			days+="\n"
		cnt +=1
	print(days)#print all list
 
 #check wrong input
def check_for_wrong_input(year,month):
    return year >= 1900 and get_days_in_month(month,year)
	
def get_days_in_month(month,year):#Used to get number days in year and check if the month user input is illegal
          if month in ['September', 'April', 'June', 'November']:
              return 30
            
          elif month in ['January', 'March', 'May', 'July', 'August','October','December']:
              return 31        

          elif month == 'February' and check_leap_year(year) == True:
              return 29

          elif month == 'February' and check_leap_year(year) == False:
              return 28

          else:
              return 0 #month user input is illegal

def main():
	year = int(input("Enter Year :"))
	month = input("Enter Month :")
	if (not check_for_wrong_input(year,month)):
		print("check your year or month input and try again :D")
		return 0
	first_day = get_first_day_in_month(year,month)
	print_days_in_month(first_day,year,month)

main()
