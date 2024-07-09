class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkString(left, right, s, skips):
            if skips > 1:
                return False
            while left <= right:
                if s[left] != s[right]:
                #either increment left pointer by 1 / decrement the right pointer by 1
                    return checkString(left + 1, right, s, skips + 1) or checkString(left, right - 1, s, skips + 1)
                else:
                    left += 1
                    right -= 1
            return True
    
        return checkString(0, len(s)-1, s, 0)
            