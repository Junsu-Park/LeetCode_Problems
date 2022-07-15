class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I' : 1,
                        'V' : 5,
                        'X' : 10,
                        'L' : 50,
                        'C' : 100,
                        'D' : 500,
                        'M' : 1000}
        prev_1 = 0
        prev_2 = 0
        ans = 0
        for i in s:
            print(i, ans)
            ans += roman_dict[i]
            if prev_1 != prev_2:
                prev_1 = 0
            if prev_2 < roman_dict[i]:
                ans = ans - prev_1 * 2 - prev_2 * 2
            prev_1 = prev_2
            prev_2 = roman_dict[i]
        return ans