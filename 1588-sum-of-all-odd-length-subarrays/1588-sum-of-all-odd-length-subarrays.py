class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range((len(arr) - 1)//2 + 1):
            for j in range(len(arr)-2*i):
                ans += sum(arr[j:j+2*i+1])
        return ans
            