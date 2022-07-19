class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        length = len(columnTitle)
        for i in range(length):
            ans += 26 ** i * (ord(columnTitle[-i-1].lower()) - 96)
        return ans