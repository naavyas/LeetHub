"""
UMPIRE: 
Understand - Find the length of the longest substring with no repeating chars
Questions: Is there a certain space or time complexiety you want us to reach or match 
Just to clarify: Input - the string 
Output - the length of the longest substring 

Match: The initial solution that comes to my mind is - 
Set: to store the values of the elements that have be iterated over 

Pseudo code: 
Every time we iterate over a value we add that element to a set if it doesn't already exist in the set and we have a counter that helps check the length of unique chars in the string.
visited = set() 
for c in s: 
    if c not in s:
        ctr increments 
        visited.add(c)
    else:
        ctr = 1 (i want to include the current element in the new length of the unique substring)
"""       

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        a = []
        count = collections.defaultdict(int)
        tlen = 0
        for r in range(0,len(s)):
            count[s[r]] += 1
            while count[s[r]] > 1 :
                t = s[l]
                count[t]-=1
                tlen-=1
                l+=1
                if count[t] == 0:
                    count.pop(t)

            tlen+=1
            a.append(tlen)
        return max(a) if a else 0

        
        
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        k = 0
        j = 0
        ctr = 0
        p1 = s[k]
        p2 = p1
        lengths = []
        visited = set()
        while j<len(s):
            if p2 not in visited:
                visited.add(p2)
                ctr += 1
                j = j+1
                if j < len(s):  
                    p2 = s[j]
            else:
                lengths.append(ctr)
                visited = set()
                ctr = 0
                p1 = s[k+1]
                p2 = p1
                k = k+1
                j = k
        if len(lengths) == 0:
            return ctr
        elif ctr == lengths[len(lengths)-1]:
            max_l = lengths[0]
            for l in lengths:
                if max_l<l:
                    max_l = l
            return max_l
        else:
            lengths.append(ctr)
            max_l = lengths[0]
            for l in lengths:
                if max_l<l:
                    max_l = l
            return max_l
"""
