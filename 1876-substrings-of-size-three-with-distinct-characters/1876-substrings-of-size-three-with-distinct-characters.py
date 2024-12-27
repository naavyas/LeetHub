"""
UNDERSTAND
2 conditions 
- no repeated chars - dict 
- k = 3 (fixed window)
return the total number of good substrings in a string (ctr variable)
IMPLEMENT
- first use a for loop that goes through all the elements in the string 
- then have an inner while loop that runs k times 
- inside this we slide the window 

DRY RUN 
x [y z z] a z
l : 1
r : 3
h =  x : 0 y: 1  z : 2 
i = 2 
ctr = 1



"""
from collections import defaultdict
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        ctr = 0
        i = 3
        h = collections.defaultdict(int)
        if len(s) < 3:
            return 0
        for i in range(3):
            h[s[i]]+=1
            
        if len(h) == 3:
            ctr+=1
        for r in range(3,len(s)):
            h[s[r]]+=1
            h[s[l]]-=1
            if h[s[l]] == 0:
                del h[s[l]]
            l+=1
            if len(h) == 3:
                ctr+=1
        return ctr
            
               
           
            
                
            
        