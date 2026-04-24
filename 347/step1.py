from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = {}
        for num in nums:
            if num in numsDict:
                numsDict[num] = numsDict[num] + 1
            else:
                numsDict[num] = 1
        topK = []
        for key, value in numsDict.items():
            if len(topK) >= k:
                heapq.heappushpop(topK, (value, key))
            else:
                heapq.heappush(topK, (value, key))
        return [key for value, key in topK]