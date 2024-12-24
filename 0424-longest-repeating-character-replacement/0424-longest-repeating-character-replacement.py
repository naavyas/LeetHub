"""
Umpire 
Understand : we can take a substring and replace at most k charecors to from the new longest substring 
"""
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 
        l = 0
        tlen = 0 
        a = []
        t = k
        max_count = 0
        max_len = 0
        count = collections.defaultdict(int)
        for r in range(0, len(s)):
                count[s[r]] += 1
                max_count = max(max_count, count[s[r]])
                while((r - l + 1)-max_count > k):
                    count[s[l]]-=1
                    l+=1
                    
                max_len = max(max_len, r-l+1)
        return max_len
                    
                    