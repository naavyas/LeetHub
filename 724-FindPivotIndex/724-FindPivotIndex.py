# Last updated: 3/29/2025, 12:38:19 PM
"""
1st attempt 
while pivot_index<len(nums): # [1,2,3] --> O(N)
            if pivot_index == 0:
                left_sum = 0
                right_sum = sum(nums[1:]) #--> O(N)
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
--------------------------------------------------
left_sums = defaultdict(int)
        pivot_index = 0 
        mid_index = len(nums) // 2
        left_sum = 0
        while pivot_index <= mid_index:
            left_sums[left_sum] = pivot_index
            left_sum += nums[pivot_index]
            pivot_index += 1
        right = len(nums)-1
        left_keys = left_sums.keys()
        right_sum = nums[right]
        while right>=mid_index:
            if right_sum in left_keys:
                return right
            right_sum += nums[right]
            right -= 1

-----------------------------------------------------
have two arrays sum_left and sum_right 
sum_left [0,1,8,11,17,22]
sum_right [0,6,11,17,] -- find the first matchung sum and return left array index
ex 2:
[2,1,-1]
left = [0,2,3]
right = [0,-1,0]
[1,-1,2]
left =[1,0]
right = [2,1]
ex3
[2,5,6,3,4]
left = [0,2,7,13,16]

right = [0,4,7,13,]
right = [18,11,7,4,0]
ex4 
[1,2,3]
left = [0,1,3]
right = [0,3,5]

-----------------
steps 1 : find the sum of the whole array 
sum_arr = 28[total_sum]
27      22
20      17
17
left = 3
right = 3
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        total_sum = sum(nums) #6
        left = 0 
        left_sum = 0  
        right_sum = total_sum - nums[left] #5
        #[1,2,[3]]
        while left<len(nums):
            if left_sum == right_sum:
                return left
            left_sum += nums[left] #6
            left+=1
            if left<len(nums):
                right_sum -= nums[left] #-3
        return -1
            




        

        



        