class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Understand: Input: the array to rotated(nums) and the number of steps to rotate by i.e k
        Output: don't return anything just cahnge nums 
        What is the space and time complexity we should follow? 
        
        Match: I would use an array with a speciic condition that continous till the condition is competed k             times.
        Plan:
        I would have an inside loop that first moves all the elements by one place and then stores the last             element in a sperate variable that can be moved to the begining. 
        
        """
        """
        if k == len(nums):
            print(nums)
        else:
            k = k % len(nums)
            temp = k
            while temp != 0:
                last = nums[len(nums)-1]
                for i in reversed(range(1, len(nums))):
                    nums[i] = nums[i-1]
                nums[0] = last
                temp = temp - 1
            print(nums)
            
        n = len(nums)
        k = k % n  # Handle rotations larger than the array size

        # Use a stack to reverse the order of the first n-k elements
        stack = []
        t = []
        # First push the last k elements to maintain their order in the final array
        for i in range(n-k, n):
            stack.append(nums[i])
        for i in range(n-k,n):
            t.append(stack.pop())
        for i in range(n-k):
            t.append(nums[i])
"""
             
        n = len(nums)
        k = k % n  # Ensure k is not greater than the array length

        # Rotate the array using slicing
        nums[:] = nums[-k:] + nums[:-k]

        return nums 

