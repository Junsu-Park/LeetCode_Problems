class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0, 1]
        tmp = 0
        for i in range(1, n):
            ans += [2 ** i + j for j in reversed(ans)]
        return ans