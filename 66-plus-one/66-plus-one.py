class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cnt = len(digits) - 1
        while cnt >= 0:
            digits[cnt] += 1
            if digits[cnt] == 10:
                digits[cnt] = 0
                cnt -= 1
            else:
                break
        if cnt == -1 and digits[0] == 0:
            return [1] + digits
        return digits
            