"""
understanding the q:
given integer array nums 
return an array - answer 
constraints - must run in O(n) time complexiety 
each element of the array is the product of the remaining elements 
potential ways to solve this 
we can have a pointer that moves through the array 
p = 0 
then everything to the left is multiplied
p = 1
then everything to the left and right of p is multiplied and added to the new matrix 
and so on 
dynamic programming 
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = 1
        postfix_prod = 1 
        products = [0]*len(nums)

        for i in range(len(nums)):
            products[i] = prefix_prod 
            prefix_prod *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            products[i] *= postfix_prod
            postfix_prod *= nums[i]
        return products

            


       