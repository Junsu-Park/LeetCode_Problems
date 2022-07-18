class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev2 = 1
        tmp = 1
        if n <= 3:
            return n
        for i in range(n-1):
            tmp = prev1 + prev2
            prev1 = prev2
            prev2 = tmp
        return tmp