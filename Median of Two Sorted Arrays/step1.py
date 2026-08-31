from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        half = (n + m + 1) // 2
        
        left = 0
        right = len(nums1) - 1
        mid = None
        
        while left < right:
            mid = (left + right) // 2
            if nums1[mid] > nums2[half - mid + 1]:
                right = mid
            elif nums2[half - mid] > nums1[mid + 1]:
                left = mid + 1
            else:
                break
        
        if (n + m) % 2 == 0:
            return float((max(nums1[mid], nums2[half - mid]) + min(nums1[mid + 1], nums2[half - mid + 1])) / 2)
        else:
            return float(max(nums1[mid], nums2[half - mid]))