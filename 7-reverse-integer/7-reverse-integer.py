class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        x = str(x)
        if x[0] == '-':
            sign = -1
            x = x[1:]
        x = str(x)
        x = int(x[::-1])
        if x > 2 ** 31 + 0 ** (sign + 1):
            return 0
        return sign * int(x)
        