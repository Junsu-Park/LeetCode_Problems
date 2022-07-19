class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        
        ans = ""
        # sign 결정
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            ans += '-'
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # 소수 만들기
        ans += str(numerator // denominator)
        if not numerator % denominator:
            return ans
        
        numerator = numerator % denominator
        
        ans += '.'
        num_dict = {numerator:len(ans)}
        while numerator > 0:
            ans += str(numerator* 10 // denominator)
            numerator = (numerator* 10 % denominator)
            if numerator in num_dict:
                idx = num_dict[numerator]
                ans = ans[:idx] + '(' + ans[idx:] + ')'
                break
            num_dict[numerator] = len(ans)
        return ans