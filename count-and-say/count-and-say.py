class Solution:
    def countAndSay(self, n: int) -> str:
        return self.recur(1, n, "1")
    
    def recur(self, tmp, end, number):
        
        if end == 1:
            return "1"
        if tmp == 1:
            return self.recur(2, end, "1")
        
        ans = ""
        prev_am = 1
        prev_num = number[0]
        for i in number[1:]:
            if i == prev_num:
                prev_am += 1
            else:
                ans += "%d%s" % (prev_am, prev_num)
                prev_am = 1
                prev_num = i
        ans += "%d%s" % (prev_am, prev_num)
        if tmp == end:
            return ans
    
        return self.recur(tmp + 1, end, ans)
        
        