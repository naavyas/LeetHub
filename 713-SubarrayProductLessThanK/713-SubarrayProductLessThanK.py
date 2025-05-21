# Last updated: 5/21/2025, 4:02:52 PM
"""
the length of the window depends on the threshold 
we have to slide the window once the product becaomes greater than the 
threshold 
Plan: 
Have a loop that goes through all the elements 
Checks for whether the element is less than the threshold and then increments the counter accordingly 
counter should also increment of the current element and the next also match the threshold
Have a seperate loop that goes through all the elements in the array and increments the counter based on whether the indivisual elememts are under the threshold or not 
DRY RUN
[10,5,2,[6]]
r = 4
l = 1
counter = 5
product = 6
k = 100
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        counter = 0
        l = 0
        r = 0
        product = 1
        if k == 0:
            return 0
        while r<len(nums):
            product *= nums[r]
            while product >= k and l<=r:
                product = product // nums[l]
                l+=1
            if product<k:
                counter += r - l + 1
            r+=1
        return counter
            