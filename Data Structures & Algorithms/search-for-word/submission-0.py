class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        visited = [n * [0] for i in range(m)]
        path = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(i, j):
            path.append(board[i][j])
            visited[i][j] = 1
            if "".join(path) == word:
                return True

            for dr, dc in directions:
                r, c = dr + i, dc + j
                if r < m and r >=0 and c < n and c >= 0 and visited[r][c] != 1:
                   if dfs(r, c):
                    return True

            visited[i][j] = 0
            path.pop()
            return False


        for i in range(m):
            for j in range(n):
                if dfs(i, j):
                    return True

        return False