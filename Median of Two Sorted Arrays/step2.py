from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        half = (n + m + 1) // 2
        
        left = 0
        right = m
        
        while left <= right:
            i = (left + right) // 2
            j = half - i
            
            L1 = nums1[i - 1] if i > 0 else float("-inf")
            R1 = nums1[i] if i < m else float("inf")
            L2 = nums2[j - 1] if j > 0 else float("-inf")
            R2 = nums2[j] if j < n else float("inf")
            
            if L1 > R2:
                right = i - 1
            elif L2 > R1:
                left = i + 1
            else:
                if (m + n) % 2 == 1:
                    return max(L1, L2)
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2