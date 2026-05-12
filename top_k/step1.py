from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        count = list(count.items())
        count.sort(key=lambda x: x[1], reverse=True)
        return [top[0] for top in count[:k]]