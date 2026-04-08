class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] != ".":
                    #check row
                    for q in range(n):
                        if q == j:
                            continue
                        if board[i][q] == board[i][j]:
                            return False
                    #check column
                    for p in range(m):
                        if p == i: 
                            continue
                        if board[p][j] == board[i][j]:
                            return False
                    # check small grid
                    x = i // 3 
                    y = j // 3
                    for w in range(x * 3, x*3 + 3):
                        for z in range(y * 3, y * 3 + 3):
                            if w == i and z == j:
                                continue
                            if board[w][z] == board[i][j]:
                                return False
        return True


