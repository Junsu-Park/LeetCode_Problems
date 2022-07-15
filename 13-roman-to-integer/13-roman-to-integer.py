class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I' : 1,
                        'V' : 5,
                        'X' : 10,
                        'L' : 50,
                        'C' : 100,
                        'D' : 500,
                        'M' : 1000}
        ans = 0
        for i, r in enumerate(s[:-1]):
            if roman_dict[s[i+1]] > roman_dict[r]:
                ans -= roman_dict[r]
            else:
                ans += roman_dict[r]
        
        return ans + roman_dict[s[-1]]