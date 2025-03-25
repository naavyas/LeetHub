# Last updated: 3/25/2025, 11:42:37 AM
"""
Here the array contains multiple 1s and 0s 
we have a variable k sized sliding window so we have an inner while loop that helps identify the size and also keeps track of the number of replacements that can happen with k. 
l = 0
        tlen = 0 
        a = []
        t = k
        for r in range(len(nums)):
            if nums[r]!=1:
                t -= 1
                while(t<=0):
                    if nums[r] != 1:
                        t+=1
                        l+=1 
                a.append(tlen)
                    
                    
            tlen+=1
            
        return max(a)
                

                
        
Dry run: 
[1,1,1,0,0,0,1,1,1,0]    k=2
find the subarray with the most number of 1s once the k's are flipped 
we have a variable sliding window approach 
the condition will be that once we find the window where all the zeros have been flipped we find the length of that window before we move forward 

[0,0,0,1]
left = 0 
right = 0
nflips = 4
"""

class Solution: 
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0 
        right = 0 
        num_flips = k
        max_len = 0
        while left<=right and right<len(nums):
            #[0,0,1,1,0,[0,1,1,1,0,1,1,0,0],0,1,1,1,1] and k = 3
            #left = 0
            #right = 6
            #nflips = 1
            #max_len = 8
            if nums[right] == 0 and num_flips >= 0:
                num_flips -= 1
            
            while num_flips < 0:
                max_len = max(max_len, right - left)
                if nums[left] == 0:
                    num_flips += 1
                left += 1      
            right += 1
        max_len = max(max_len, right - left)
        return max_len



        