"""
Student: Sarel Alush
ID: 316373851
Assignment no. 1
Program: 3.py
"""


import  random

#print the board
def printBoard(arr,win=False):
    for i in range(1, len(arr)-1):
        print("   +"+(len(arr)-2)*"---+", end="")
        print("\n{:<2}".format(i), end=" ")
        for j in range(1, len(arr)):
            print("|", end="")
            if not j == len(arr):
                if (arr[i][j] != "*" or win):
                    print(" {0} ".format(arr[i][j]), end="")
                else:
                    print(" {0} ".format(" "), end="")
        print()
    print("   +"+(len(arr)-2)*"---+",end="\n  ")
    for j in range(1, len(arr)-1):
        print("{:>4}".format(j), end="")
    print()
    
def create_random_list(bombs, n):
    grip = [[' ' for i in range(0, n)] for j in range(0, n)]#create marix N+2 X N+2 
    rndi = random.randint(1, n - 2) #rnd i cord
    rndj = random.randint(1, n - 2) #rnd j cord
    for i in range(0, bombs):
        while grip[rndi][rndj] == "*": #if have bomb there
            rndi = random.randint(1, n - 2)#again rnd i
            rndj = random.randint(1, n - 2)#again rnd j
        grip[rndi][rndj] = "*"
    return grip #return matrix

#check how much bombs around
def update_number_of_bomp_around(arr,i,j):
    sum_bomb = 0
    my_check = 1
    for k in range(0,3):
        for l in range(0,3):
            if arr[k+i-1][l+j-1] == "*": #if find bomb
                sum_bomb +=1 
                my_check = 0
    arr[i][j] = sum_bomb
    return my_check #return for stop recursiv not

#check if board is full
def check_for_full_board(arr):
    sum_col_full=0
    for i in arr:
        if not (" " in i[1:-1]):#if have " " in list
            sum_col_full+=1 
    return sum_col_full == (len(arr)) #if len of list

#recursive for all space
def recursive(arr,i,j):
    movelist = [(1,0),(-1,0),(0,1),(0,-1)] #list of (x,y) 
    if i <1 or i >len(arr)-2 or j<1 or j>len(arr)-2 :#if we out of list range return
        return 1
    if arr[i][j] =="*": #if we are on bomb return 0
        return 0
    if arr[i][j] == "-" or not arr[i][j]==' ': #if we stepped again
        return 1
    arr[i][j] = "-" #stepped to know we were here
    for k,l in movelist:#run all list (x,y)
        if(update_number_of_bomp_around(arr,i,j)):#update and check if have bombs around
            recursive(arr,i+k,j+l)#call to recursive func with new cord
    return 1

#print the result
def check_res(arr,win):
    if(win):#win
        print("you Won the Game!!!")
        print("your Board:")
        printBoard(arr,True)
    else:#lose
        print("you Lose the Game!!!")
        print("Try Again")
        print("your Board:")
        printBoard(arr,True)

def main():
    Bombs = int(input("Enter number of bombs: "))#enter number of bombs
    Game_Bord = int(input("Enter NxN: "))#size Board
    while Bombs >= Game_Bord*2:#check if number of bombs small than sizeBoard*2
        print("U need less bombs")
        Bombs = int(input("Enter number of bombs: "))
        Game_Bord = int(input("Enter NxN: "))
    arr = create_random_list(Bombs,Game_Bord+2)#create new list with random bombs
    check_win = 1#if we lose the game be 0
    winner = 0  #if we win the game be 1
    while check_win and not winner: #check if we win or lose the while stop
        printBoard(arr)
        x = int(input("Enter cord x: "))
        y = int(input("Enter cord y: "))
        check_win = recursive(arr,x,y)#call to recursive func if return 0 lose
        winner = check_for_full_board(arr[1:-1])#check if board is full and return 1 if its true
    if not check_win:#lose
        check_res(arr,check_win)
    else:#win
        check_res(arr,winner)
main()
