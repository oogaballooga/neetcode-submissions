class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #text1 will be horz or j
        #text2 will be vert or i
        n1, n2 = len(text1), len(text2)

        dp = [[0] * (n1+1) for _ in range(n2+1)]
        for i in range(n2):
            for j in range(n1):
                if text1[j] == text2[i]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return dp[n2][n1]