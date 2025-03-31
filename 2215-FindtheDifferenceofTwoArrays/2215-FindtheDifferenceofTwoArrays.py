# Last updated: 3/31/2025, 12:57:35 AM
"""
find the diff in two int arrays
first index all unique values in nums1 not present in nums2
2nd is all values in nums2 not present in nums1

can go through both the lists seperately and check if that value is in list 2-- O(N^2) complexiety 

"""
from collections import defaultdict 
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dict_nums1 = defaultdict(int)
        dict_nums2 = defaultdict(int)
        for r in range(len(nums1)):
            dict_nums1[nums1[r]] += 1
        for r in range(len(nums2)):
            dict_nums2[nums2[r]] += 1
        unique_nums1 = set()
        for r in nums1:
            print('the val is : ', r, 'the dict val is :' ,dict_nums2[r])
            if dict_nums2[r] == 0:
                unique_nums1.add(r)
        unique_nums2 = set()
        for r in nums2:
            if dict_nums1[r] == 0:
                unique_nums2.add(r)
        final_list = []
        final_list.append(list(unique_nums1))
        final_list.append(list(unique_nums2))
        return final_list





        