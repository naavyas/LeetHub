"""
Understand : 
we go through all the elements of the array and find the consective 
elements that have the largest sum 
- Does the elements that are taken in the subarray have to be consective i/e right next to each other? Yes
- What is the space and time complexiety we are looking for? 
Match: 
This is a sliding window problem because we know that the elements we are looking for to create the cub array are next to each other 
We also know that the size of the sliding window doesn't matter which means that there will be a vraible whose size will dynamically change to find the sum
Plan: 
we can have a loop that goes through all the elements and a variable that is the length of the sliding window 
Then we have a variable that stores the sum of the elements that we add together
If the sum falls by adding a new element we change the length of the window and start looking at a new sub array 
we also need to store the sums in an array and then return the max element of that array 

we should have two pointers - 
right pointer that increments and left pointer
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        val = nums[0]
        currSum = 0
        for n in nums:
            if currSum<0:
                currSum = 0
            currSum += n 
            val = max(val, currSum)
        return val

        

        