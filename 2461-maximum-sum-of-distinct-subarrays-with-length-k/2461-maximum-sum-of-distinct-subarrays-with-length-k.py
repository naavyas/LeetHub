"""
Dry run:
[1,5,4,[2,9,9],9]
r : 4 
l : 1
k = 3
max_sum = 15
ctr = 0
max_sum : 10
elements =  2 : 1, 9 : 2
            
"""
from collections import defaultdict
class Solution:
    
            
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        elements = collections.defaultdict(int)
        sum_elements = 0
        max_sum = 0
        l = 0
        for i in range(k):
            sum_elements += nums[i]
            elements[nums[i]] += 1
        if len(elements) == k:
            max_sum = max(max_sum, sum_elements)
        for r in range(k, len(nums)):
            elements[nums[r]]+=1
            sum_elements+= nums[r]
            elements[nums[l]]-=1
            sum_elements -= nums[l]
            if elements[nums[l]]==0:
                del elements[nums[l]]
            l+=1
            if len(elements) == k:
                max_sum = max(max_sum, sum_elements)
        return max_sum
                
            
        
            
        """l = 0 
        sum_sub = 0
        max_sum = 0
        elements = collections.defaultdict(int)
        for r in range(len(nums)):
            for i in range(r, r+k):
                elements[r]+=1
                if elements[r] == 1:
                    sum_sub += nums[r]
                    
                else:
                    max_sum = max(sum_sub, max_sum)
                    sum_sub -= elements[l]
                    if elements[l]==0:
                        del elements[l]
                    l+=1"""
                    
                
                
            
        
            
        
        """
        l = 0
        sum_sub = 0
        ctr = 0
        max_sum = 0
        elements = collections.defaultdict(int)
        for r in range(len(nums)):
            elements[r]+=1
            if elements[r] == 1 and ctr < k:
                sum_sub += nums[r]
                ctr+=1
                    
            else:
                max_sum = max(sum_sub, max_sum)
                sum_sub -= elements[l]
                if elements[l]==0:
                    del elements[l]
                l+=1
                
            
                
        return max_sum
      """          
                
            
            
        