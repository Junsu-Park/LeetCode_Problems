class Solution:
    def numTrees(self, n: int) -> int:
        dp = {0:1, 1:1, 2:2}
        for i in range(3, n+1):
            dp[i] = 0
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]
        return dp[n]
        