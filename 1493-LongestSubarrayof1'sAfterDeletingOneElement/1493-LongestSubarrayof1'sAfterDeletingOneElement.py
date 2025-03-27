# Last updated: 3/27/2025, 3:30:31 PM
"""
go through the array to find the longest substring that has only 1s 
this can be formed by deleting at max only 1, 0
return the length of this max subarray 
input: array with 1s and 0s 
output : the length of the max subarray returned 
DELETE not FLIP 
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        no_of_deltes = 1 
        """
        at most 1 zero is deleted in each window 
        The length of the window is taken such that the zero is not included
        [1,[0,0,1],0]
        nd = 0
        maxlen = 1
        """
        if nums == [0] * len(nums):
            return 0
        left = 0 
        right = 0 
        max_len = 0
        no_of_deletes = 1
        while left<=right and right<len(nums):
            if nums[right] == 0 and no_of_deletes > -1:
                no_of_deletes -= 1
            while no_of_deletes == -1:
                max_len = max(max_len,right - left-1)
                if nums[left] == 0:
                    no_of_deletes+=1
                left+=1
            right += 1
        
        if nums[len(nums)-1] == 1:
            right = len(nums)-1
            max_len = max(max_len, right - left)
        
        return max_len
            


        
        