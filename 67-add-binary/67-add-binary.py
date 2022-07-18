class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = (len(a) - len(b)) * '0' + b
        if len(a) < len(b):
            a = (len(b) - len(a)) * '0' + a
        
        ans = ''
        carry = 0
        for i in range(1, len(a)+1):
            ans += str((int(b[-i]) + int(a[-i]) + carry) % 2)
            carry = (int(b[-i]) + int(a[-i]) + carry) // 2
        if carry:
            ans += '1'
        
        return ans[::-1]