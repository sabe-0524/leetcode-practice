from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index1 in range(len(numbers)):
            for index2 in range(index1 + 1, len(numbers)):
                current = numbers[index1] + numbers[index2]
                if current == target:
                    return [index1 + 1, index2 + 1]
                if current > target:
                    break