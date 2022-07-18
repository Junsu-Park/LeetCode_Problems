class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        start = 1
        end = x - 1
        mid = 1
        while start <= end:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid - 1
            elif mid * mid < x:
                start = mid + 1
            else:
                return mid
        if mid * mid > x:
            return mid - 1
        else:
            return mid