"""
Student: Sarel Alush
ID: 316373851
Assignment no. 1
Program: grades.py
"""

#read all students from file
def read_students_from_file():
      dic_students = {}
      f = open("students.txt","r")
      for line in f.readlines():#read lines
            dic_students[line.split()[0]] = " ".join(line.split()[1:]) #enter line to dict
      return dic_students

#read all grades from file
def read_grades_from_file():
      dic_grades = {}
      f = open("grades.txt","r")
      for line in f.readlines():#read lines
          dic_grades[line.split()[0]] = [int(g) for g in line.split()[1:]]#enter line to dict
      return dic_grades

#check for best grade and print
def print_best_grade(students,grades):
      average_of_best_grades = 0
      id_of_best_student = 0 
      curr_grade = 0
      for k,v in grades.items():#run all grades and keys(id)
            curr_grade = 0
            for grade in v:#run grade of curr students
                  curr_grade += grade #sum of grade
            if curr_grade/len(v)>average_of_best_grades: #check if this the best average in this loop
                  average_of_best_grades = curr_grade/len(v)
                  id_of_best_student = k
      print("name of student is {0} and the average is : {1}".format(students[id_of_best_student],average_of_best_grades))
      
#return dict with all grades and how much time does each one have
def create_dict_sum_of_grade(grades):
      dict_sum_grades = {}
      for k,v in grades.items():#run all grades and keys
            for grade in v: #run grade of curr students
                  if grade in dict_sum_grades: #if grade exist in dict
                        dict_sum_grades[grade]+=1
                  else:
                        dict_sum_grades[grade]=1
      return dict_sum_grades

#check for most grade and print
def print_most_grade(grades):
      most_grade_val = 0
      dict_sum_grades = {}
      dict_sum_grades = create_dict_sum_of_grade(grades)
      for k,v in dict_sum_grades.items():#run all dict and check where have the big value
            if v > most_grade_val:
                  most_grade_val = v
                  most_grade_key = k
      print("the most grade is : {0}".format(most_grade_key))#print the most grade
      
#print all the grade not in list(dict..)
def print_no_grade(grades):
      dic_all_grades = create_dict_sum_of_grade(grades)
      print("All grades that are not in the grades list are:")
      for i in range(0,101):
            if i not in dic_all_grades.keys():#check if the grade between 0-100 in dic
                  print(i,end=" ")#if not print number
def main():
      dic_students = read_students_from_file()
      dic_grades = read_grades_from_file()
      print_best_grade(dic_students,dic_grades)
      print_most_grade(dic_grades)
      print_no_grade(dic_grades)
main()
