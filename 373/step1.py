from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        answer = []
        min_heap = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(min_heap, (nums1[i]+nums2[0], i, 0))
        
        for j in range(k):
            sum_val, index1, index2 = heapq.heappop(min_heap)
            answer.append([nums1[index1], nums2[index2]])
            if index2 < len(nums2) - 1:
                heapq.heappush(min_heap, (nums1[index1]+nums2[index2+1], index1, index2+1))
            
        return answer