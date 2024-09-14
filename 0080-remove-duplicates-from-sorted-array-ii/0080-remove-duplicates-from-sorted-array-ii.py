"""
Understand: 
-> Input: The array nums containing the values 
->Output: k i.e the number of elements remaining after the duplicates have been removed 
->Problem statement: The max number of duplicates can only be 2. Anything beyond that has to be removed (i.e the third element). The remaining elemnts left after removing the duplicate have to then be moved up a spot. 

Match: When we use a  
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n

        i = 2
        for j in range(2, n):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1

        return i
                        
    """
       d=defaultdict(int)
        ctr = len(nums)
        for i in range(len(nums)):
            flag = False
            if d[nums[i]] == 0:
                d[nums[i]] = 1
            else:
                if(d[nums[i]]<2):
                    d[nums[i]] += 1  
                else:
                    k = i
                    for j in range(k+1,len(nums)):
                        nums[k] = nums[j]
                        k += 1
                    ctr -= 1
                    flag = True
            if flag:
                if d[nums[i]] == 2:
                    p = i
                    for j in range(p+1,len(nums)):
                        nums[p] = nums[j]
                        p += 1
                    ctr -= 1
                else:
                    d[nums[i]] += 1
        return ctr
        """
         



        