from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect_dict = {}
        answer = []
        for num1 in nums1:
            intersect_dict[num1] = True
        
        for num2 in nums2:
            if num2 in intersect_dict and intersect_dict[num2] == True:
                answer.append(num2)
                intersect_dict[num2] = False
        
        return answer