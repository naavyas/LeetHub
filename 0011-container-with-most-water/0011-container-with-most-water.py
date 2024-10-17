"""
Understand: 
We are given an array with n different lines. The heaight of each line is the value in height[i]. We get have to find the two lines whose area forms a container that can hold the max water 
Question: Why are the coordinates given in the information important to the question 
Input: Array of heights 
Output: the max water in the contained is returned as the area 

Match: 
Brute force approach - 
take two pointers ;
the first pointer takes the height of the first line and the second compares if the height of the second line is lesser than the first - if it that height is chosen as x and the distance between height[i] and height[j] is taken as y. Then area = x*y and we take the max area and return that
Refined apprach - Move the pointer that points to the smaller line 
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        k = 0
        j = len(height)-1
        areas = set()
        while(k<=j):
            i = height[k]
            p = height[j]
            b = abs(k-j) 
            if (i>p):
                l = p
                area = l*b 
                areas.add(area)
                j-=1
            else:
                l = i
                area = l*b
                areas.add(area)
                k+=1
        return max(areas)
                
            
            
            
            
            
        
        