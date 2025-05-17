# Last updated: 5/16/2025, 10:43:59 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o','u']
        right = 0
        left = 0 
        max_count = 0
        vowel_count = 0
        for r in range(k):
            if s[r] in vowels:
                vowel_count += 1
        max_count = max(max_count, vowel_count)
        right = k-1
        left = 0
        while right<len(s):
            right += 1
            while right<len(s) and left<right and right - left + 1 > k :
                if s[left] in vowels:
                    vowel_count -= 1
                left+=1
                if s[right] in vowels:
                    vowel_count += 1
            max_count = max(max_count, vowel_count)
        return max_count

"""
l e e t c o d e.      k = 3
vowelcount = 1 
right = 5
left = 1
max = 2
"""


        