# Last updated: 3/28/2025, 12:38:38 PM
"""
given an array of integers calculate the pivot index of the array 
pivot index : this is the index where the sum of the numbers strictly to the left = sum right
return the LEFT MOST pivot index if there is no index where the sum of the either side is equal then return -1
test cases
[0,1,-1]
[-2,2,-2]
[-1,1,5,-2,2]
first i come to 0 if its at index 0 i take left_sum = 0 and add everything on the right 
if left_sum == right_sum then then i return the current index 
if not i move ahead and continue the process 
if i reach the last index and the sum isn't equal i return -1 
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        pivot_index = 0 
        while pivot_index<len(nums):
            if pivot_index == 0:
                left_sum = 0
                right_sum = sum(nums[1:])
                if left_sum == right_sum:
                    return pivot_index
            elif pivot_index == len(nums)-1:
                right_sum = 0
                left_sum = sum(nums[:-1])
                if left_sum == right_sum:
                    return pivot_index
            else:
                left_sum = sum(nums[0:pivot_index])
                right_sum = sum(nums[pivot_index+1:])
                if left_sum==right_sum:
                    return pivot_index
            pivot_index += 1
        return -1 



        