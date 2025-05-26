# Last updated: 5/26/2025, 2:44:32 PM
"""
we dont need to store the actual subarrays but only the number of subarrays 
so we just keep moving the left ahead when we see the product goes greater and we incremenr the counter by the length of the window because that will give us the combination of the terms 

"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0 
        right = 0 
        prod = 1
        ctr = 0 #counts the number of subarrays 
        while right<len(nums):
            prod = prod*nums[right]
            while prod>=k and left<=right:
                prod = prod // nums[left]
                left += 1

            ctr = ctr + (right-left+1)
            right+=1
        return ctr 
                

        