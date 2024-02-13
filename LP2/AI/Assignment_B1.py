
def printSolution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q",end=" ")
            else:
                print(".",end=" ")
        print()


def isSafe(board,row,col):
    for i in range(col):
        if board[row][i] ==1:
            return False
        
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False
        
    for i,j in zip(range(row,len(board),1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    
    return True
    

def solveNqUtil(board,col):
    if col>=len(board):
        return True

    for row in range(len(board)):
        if isSafe(board,row,col):
            board[row][col] = 1

            if solveNqUtil(board,col+1) == True:
                return True
            
            board[row][col] = 0
    return False



def solveNQ(N):
    board = [[0 for j in range(N)] for i in range(N)]
    if solveNqUtil(board,0) == False:
        print("Solution Does not Exist")
        return False
    
    printSolution(board)
    return True

if __name__ == "__main__":
    solveNQ(int(input("Enter the number of Queens:")))
