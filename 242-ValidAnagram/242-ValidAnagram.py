from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        if len(s)!=len(t):
            return False
        for r in range(len(s)):
            s_dict[s[r]] += 1
        for r in range(len(t)):
            t_dict[t[r]] += 1
        if s_dict == t_dict:
            return True
        else:
            return False

        