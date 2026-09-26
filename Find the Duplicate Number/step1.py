from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        while fast == 0 or fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        
        slow2 = 0
        while slow2 == 0 or slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow