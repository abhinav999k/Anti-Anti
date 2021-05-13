class Solution:
    def __init__(self,N):
        self.N = N
        self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def isValidMove(self,row,col):
        #Left row check
        for i in range(col,-1,-1):
            if(self.board[row][i] == 1):
                return False
        #Lower Diagonal check
        row_copy = row + 1
        col_copy = col - 1
        while(row_copy <= 3 and col_copy >=0):
            if(self.board[row_copy][col_copy]==1):
                return False
            row_copy = row_copy + 1
            col_copy = col_copy - 1
        #Upper diagonal check
        row_copy = row-1
        col_copy = col-1
        while row_copy >= 0:
            if(self.board[row_copy][col_copy]==1):
                return False
            row_copy -= 1
            col_copy -= 1
        return True
                
    def backTrack(self,col):
        if self.N == col:
            return True
        #Starting with col 0
        for i in range(self.N):
            if(self.isValidMove(i,col)==True):
                self.board[i][col] = 1
                if(self.backTrack(col+1)==True):
                    return True
                else:
                    self.board[i][col] = 0
        return False




    def printBoard(self):
        print(self.board)


p1 = Solution(4)
p1.printBoard()
p1.backTrack(0)
p1.printBoard()

