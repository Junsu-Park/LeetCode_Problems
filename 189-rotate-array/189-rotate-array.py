def Gcd(a, b):
    while b:
        a, b = b, a%b
    return a

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        gcd = Gcd(len(nums), k)
        
        for i in range(gcd):
            prev = nums[i]
            nums[i] = nums[i-k]
            j = 1
            while (k*j + i) % len(nums) != i:
                tmp = nums[(k*j + i) % len(nums)]
                nums[(k*j + i) % len(nums)] = prev
                prev = tmp
                j += 1
        