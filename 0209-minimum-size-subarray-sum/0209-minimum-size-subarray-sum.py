"""
Understand: 
We are given positive integer nums and target 
We have to have a sliding window whose length is variable 
This is used to find out how many CONSECTIVE elements are taken to get the target sum 

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        s = 0
        min_len = float("inf")
        while r<len(nums):
            s+=nums[r]
            while s >= target: #??
                min_len = min(min_len, r-l+1)
                s-=nums[l]
                l+=1
            r+=1
        return min_len if min_len != float('inf') else 0
        """
        l = 0
        r = 1
        s = nums[l]
        k = 1 
        a = []
        while l<len(nums) and r<len(nums):
            s += nums[r]
            k += 1
            if s >= target:
                a.append(k)
                s = s - nums[l]
                l+=1
                k-=1
            r+=1
        return min(a)
               
        
         """   
        