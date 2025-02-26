"""
initial approach to the problem - using a dictionary
"""
from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        values = collections.defaultdict(int)
        for r in nums:
            values[r] += 1
            if values[r] > 1:
                return True
        return False


        