class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_ans = None
        for i in range(len(s)):
            # odd number
            left = i - 1
            right = i + 1
            tmp_len = 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    tmp_len += 2
                    left -= 1
                    right += 1
                else:break
            tmp_ans = s[left+1:right]
            if tmp_len > max_len:
                max_len = tmp_len
                max_ans = tmp_ans
            # even number
            left = i
            right = i + 1
            tmp_len = 0
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    tmp_len += 2
                    left -= 1
                    right += 1
                else:break
            tmp_ans = s[left+1:right]
            if tmp_len > max_len:
                max_len = tmp_len
                max_ans = tmp_ans
        return max_ans