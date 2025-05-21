# Last updated: 5/21/2025, 4:05:11 PM
"""
given is an array of integers k 
we have to return the continous subarrays where the product of all the elements is strictly less than k 
we have to return all the possible subarrays 
the trick here is that eventhiugh we have to slide our window we also have to keep track of indivisual elements that might be added to the array
other test cases to think about - 
[100,25,1,60,3,10,1] k = 60
we initially start by directly appending the values of the right point to a list if it is below k 
if not below k then we just move our left ahead
[25],[1], [25,1], [3], [10], [3,10]
left = 4 
right = 5
prod = 30
to_add = [25,1]
 if prod < k:
                to_add = nums[left:right+ 1]
                if to_add not in subarrays: 
                    subarrays.append(to_add)
            else:
                while prod>=k and left<=right:
                    prod = prod // nums[left]
                    left += 1
                [10,1,40] k = 50
                    
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ctr = 0
        if min(nums) >= k:
            return 0 
        #[10,5,2,6]
        right = 0 
        left = 0 
        prod = 1
        ptr = 0
        while right<len(nums):
            prod = prod * nums[right] 
            while prod>=k:
                prod = prod // nums[left]
                left += 1
            if prod < k:
                ctr += right-left + 1
            right += 1
 
            
            
        print(ctr)
        return ctr
    """
    [100,25,1,60,3,10,1] k = 60
    right = 4 
    left = 4
    prod = 3
    [25],[1], [25,1], [3],
    """