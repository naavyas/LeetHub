# Last updated: 8/11/2025, 5:34:07 PM
"""
given an array that contains only 0s and 1s and integer k 
return the max number of consectives 1s in the array 
you can flip atmost k 0's in the array 

so we go through all the elements in the array and create a window
we keep fliiping the ones as long as k elememts are still avaiable 
once the k becomes zero we add the length of the string to a varable and only change it if we find another element that is bigger 
dry run : 
[1,1,1,0,0,0,1,1,1,1,0]
left = 3 
right = 3
c = 2
max_len = 5
[1,0,0,1,1,0] c=0
right = 4
left = 1
m = 5
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        c = k
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                c-=1
            while c<0:
                if nums[left] == 0:
                    c+=1
                left+=1
            max_len = max(max_len, right-left+1)
        return max_len
