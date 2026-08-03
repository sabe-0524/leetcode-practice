from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        d = defaultdict(int)
        minus_list = []
        plus_list = []
        zero_num = 0
        
        for num in nums:
            if num < 0:
                d[num] += 1
                minus_list.append(num)
            elif num > 0:
                d[num] += 1
                plus_list.append(num)
            else:
                zero_num += 1
        
        for minus in minus_list:
            for plus in plus_list:
                two_sum = minus + plus
                if two_sum == 0:
                    for _ in range(zero_num):
                        answer.add(tuple(sorted([minus, plus, 0])))
                else:
                    appendix = -(minus + plus)
                    appendix_num = d[appendix]
                    if appendix == minus or appendix == plus:
                        appendix_num -= 1
                    for _ in range(appendix_num):
                        answer.add(tuple(sorted([minus, plus, appendix])))
        
        zero_count = int((zero_num * (zero_num - 1) * (zero_num - 2)) / 6)
        for _ in range(zero_count):
            answer.add((0, 0, 0))
        
        return [list(triplet) for triplet in answer]