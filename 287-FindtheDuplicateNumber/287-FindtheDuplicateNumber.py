# Last updated: 5/28/2025, 4:56:10 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0 
        fast = 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: 
                break 
        slow2 = 0 
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        