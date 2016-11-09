class Solution(object):


    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if(len(board)<=1):
            return False
        for i in xrange(0,len(board)):
            if(self.isValidRow(board,i)==0):
                print "row"
                return False
        for i in xrange(0,len(board)):
            if(self.isValidColum(board,i)==0):
                print "colum"
                return False
        for i in xrange(0,len(board)-1,3):
            for j in xrange(0,len(board)-1,3):
                if(self.isValidGrid(board,i,j)==0):
                    print "grid"
                    return False
        return True

    def isValidRow(self, board, row):
    	Hashtable = [0]*9
    	for i in xrange(0,len(board)):
    		if(board[row][i]<='9' and board[row][i]>='1'):
    			if(Hashtable[int(board[row][i])-1]==0):
    				Hashtable[int(board[row][i])-1]=-1
    			else:
    				return 0
    	return 1

    def isValidColum(self,board,colum):
    	Hashtable = [0]*9
    	for i in xrange(0,len(board)):
            if(board[i][colum]<='9' and board[i][colum] >='1'):
                if(Hashtable[int(board[i][colum])-1]==0):
    				Hashtable[int(board[i][colum])-1]=-1
                else:
    				return 0
    	return 1
        
    def isValidGrid(self,board,row,colum):
    	Hashtable = [0]*9
        for i in xrange(row,row+3):
            for j in xrange(colum,colum+3):
                if(board[i][j]<='9' and board[i][j] >='1'):
                    if(Hashtable[int(board[i][j])-1]==0):
                        Hashtable[int(board[i][j])-1]=-1
                    else:
                        return 0
    	return 1