class Solution:
    def myAtoi(self, s: str) -> int:
        cnt = 0
        sign = '+'
        ans = []
        while cnt < len(s) and s[cnt] == ' ':
            cnt += 1
            
        if cnt < len(s) and (s[cnt] == '+' or s[cnt] == '-'):
            sign = s[cnt]
            cnt += 1
            
        while cnt < len(s) and s[cnt].isdigit():
            ans.append(s[cnt])
            cnt += 1
        
        if not ans:
            return 0
        
        ans = int(''.join(ans)) * int(sign + '1')
        ans = min(2**31-1, ans)
        ans = max(-(2**31), ans)
        return ans