class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        if (m+n) % 2:
            return sorted(nums1 + nums2)[(m+n)//2]
        else:
            return sum(sorted(nums1 + nums2)[(m+n)//2-1:(m+n)//2+1]) / 2
        