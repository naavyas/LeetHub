class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        s = s.strip()
        for i in reversed(s):
            if not i.isspace(): 
                l += 1
            else:
                break;
        return l
                
                
        