class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row duplicate 
        # check column duplicate

        for i in range(len(board)):
            row = {}
            column = {}
            for j in range(len(board[i])):
                if(board[i][j] != "."):
                    row[board[i][j]] = row.get(board[i][j],0) + 1
                    if row[board[i][j]] > 1:
                        return False
                if(board[j][i] != "."):
                    column[board[j][i]] = column.get(board[j][i],0) + 1
                    if column[board[j][i]] > 1:
                        return False
        
        # check cubic duplicate
        cubic_row = [0,3,6]
        cubic_column = [0,3,6]
        steps = [0,1,2]
        for i in cubic_row:
            for j in cubic_column:
                cubic = {}
                for g in steps:
                    for h in steps:
                        if board[i+g][j+h] != ".":
                            cubic[board[i+g][j+h]] = cubic.get(board[i+g][j+h],0) + 1
                            if cubic[board[i+g][j+h]] > 1:
                                return False
        return True