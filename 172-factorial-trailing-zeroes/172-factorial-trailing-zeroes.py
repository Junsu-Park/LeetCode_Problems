import math

class Solution:
    def trailingZeroes(self, n: int) -> int:
        tmp = 1
        ans = 0
        while 5 ** tmp <= n:
            ans += n // (5 ** tmp)
            tmp += 1
        return ans