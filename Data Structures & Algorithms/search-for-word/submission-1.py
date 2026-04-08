class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i: int, j: int, k: int) -> bool:
            # 当前位置字符必须匹配 word[k]
            if board[i][j] != word[k]:
                return False
            # 已匹配到最后一个字符
            if k == len(word) - 1:
                return True

            visited[i][j] = True
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    if dfs(ni, nj, k + 1):
                        return True
            visited[i][j] = False  # 回溯
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False