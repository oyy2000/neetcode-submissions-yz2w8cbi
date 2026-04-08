class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        top, bottom = 0, rows
        left, right = 0, cols
        n = rows * cols
        while len(res) < n:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            if top >= bottom or len(res) >= n:
                break
                
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            if left >= right or len(res) >= n:
                break
            for i in range(right - 1, left - 1 , -1):
                res.append(matrix[bottom-1][i])
            # x = right - 1
            # while(x <= left and x >= 0):
            #     res.append(matrix[bottom-1][x])
            #     x -= 1
            bottom -= 1
            if top >= bottom or len(res) >= n:
                break

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            print(res)

        return res
