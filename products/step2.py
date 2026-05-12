from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = []
        right_product = []
        answer = []
        product = 1
        for num in nums:
            left_product.append(product)
            product *= num
            
        product = 1
        for num in reversed(nums):
            right_product.append(product)
            product *= num
        right_product.reverse()
        for i in range(len(nums)):
            answer.append(left_product[i] * right_product[i])
        
        return answer