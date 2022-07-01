class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        ans = ''
        idx = 0
        rows = {}
        
        
        for i in range(numRows):
            rows[i] = []
            
        for j, el in enumerate(s):
            j %= 2 * (numRows - 1)
            if j > numRows - 1:
                rows[2 * (numRows - 1) - j].append(el)
            else:
                rows[j].append(el)
        for v in rows.values():
            ans += ''.join(v)
        
        return ans
            