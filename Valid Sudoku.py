class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            valscol = []
            valsrow = []
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in valscol:
                    return False
                else:
                    valscol.append(board[j][i])
                
                if board[i][j] != '.' and board[i][j] in valsrow:
                    return False
                else:
                    valsrow.append(board[i][j])
        groups = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for g1 in groups:
            for g2 in groups:
                valsh = []
                valsv = []
                for i in g1:
                    for j in g2:
                        if board[i][j] != '.' and board[i][j] in valsh:
                            return False
                        else:
                            valsh.append(board[i][j])
                        if board[j][i] != '.' and board[j][i] in valsv:
                            return False
                        else:
                            valsv.append(board[j][i])
        return True
