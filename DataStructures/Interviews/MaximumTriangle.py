class Solution:
    def maximalRectangle(self,  matrix: List[List[str]]):
        maxarea = 0
        dp = [[0] * len(matrix[0])] for _ in range(len(matrix))
        for i in range(len(matrix[0])):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    continue
                width = dp [i][j] = dp[i][j -1] + 1 for j else 1
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i - k + 1))
        return maxarea

        