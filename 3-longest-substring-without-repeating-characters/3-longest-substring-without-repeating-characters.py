class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_dict = {}
        ans = 0
        tmp_start = 0
        for i, el in enumerate(s):
            if el in str_dict and str_dict[el] >= tmp_start:
                ans = max(ans, i - tmp_start)
                tmp_start = str_dict[el] + 1
            str_dict[el] = i
        return max(ans, len(s) - tmp_start)