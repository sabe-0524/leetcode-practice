from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums))]
        for num, freq in count.items():
            buckets[freq - 1].append(num)
        answer = []
        for bucket in reversed(buckets):
            if len(bucket) == 0:
                continue
            for num in bucket:
                answer.append(num)
            if len(answer) == k:
                return answer
        
        return []