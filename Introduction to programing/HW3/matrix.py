"""
Student: Sarel Alush
ID: 316373851
Assignment no. 3
Program: matrix.py
"""

#MatT in list comprehension 
def matT_comprehension(mat):
      return [[matTest[i] for matTest in mat]for i in range(len(mat[0]))]

#MatT in list regular loop 
def matT_loop(mat):
      matT = []
      for i in range(0,len(mat[0])):
            matN = [] #new mat
            for j in range(0,len(mat)):
                  matN.append(mat[j][i])#fill mat
            matT.append(matN)#append new mat to the list of lists
      return matT
	  
#read matrix from file
def read_matrix_from_file():
      f = open("matrices.txt","r")#open file in read mode
      s = f.read()[2:].split("B=")#get two lists
      s = [st.split("\n") for st in s] #split where have \n 
      matA = [line.split() for line in s[0] if line] #split where have space 
      matB = [line.split() for line in s[1] if line] #split where have space 
      matA = [[int(matA[i][j]) for j in range(0,len(matA[0]))] for i in range(0,len(matA))] #all items in list is chars now we change the type to int
      matB = [[int(matB[i][j])for j in range(len(matB[0]))]for i in range(len(matB))] #all items in list is chars now we change the type to int
      return matrix_mult(matA,matB)#call to mutrix_mult func
      
def matrix_mult(matA,matB):
      matD = []
      sum_cnt = 0
      matA = matT_loop(matA) #get matA to MataT
      for i in range(0,len(matA)):
            matC = []#new mat
            for j in range(0,len(matA)):
                  sum_cnt = 0
                  for k in range(0,len(matA[0])):
                        sum_cnt+= matA[i][k]*matB[k][j] #mult matrix here!
                  matC.append(float(sum_cnt))
            matD.append(matC)#append to list of lists
      return matD
	  
#print mutrix in format
def print_matrix(mat):
      r = ""
      for item in mat:
            r += "".join(str(x)+" " for x in item)+"\n"
      return r[:-1]
	  
def main():
      res = print_matrix(read_matrix_from_file())
      print(res)
main()
