# Last updated: 3/25/2025, 10:20:26 AM
"""
understanding the question: 
the array nums : has n elements 
fixed window length of k 
find the window that has max avg value and return this window
"""
import math
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        [1,12,-5,-6,50,3]
        left = -5
        right = 3 
        wind_avg = 2/4 = 12.5 
        max = 12.5 
        """
        if len(nums) == 1:
            return nums[0]
        #[1,2,3] and k = 3
        left = 0 
        right = 0
        #initial window avg 
        #[-1,4,[5,-3]] k = 2
        #left = 1 right = 3
        #i = 1
        #sum_window = 2
        sum_window = 0 
        for i in range(k):
            sum_window += nums[right]
            right += 1
        window_avg = sum_window / k
        max_avg = -10 ** 4
        max_avg = max(max_avg,window_avg)

        while left<right and right<len(nums):
            sum_window += nums[right]
            right += 1
            sum_window -= nums[left]
            left += 1
            window_avg = sum_window / k
            max_avg = max(max_avg,window_avg)
        return max_avg


        

        



        