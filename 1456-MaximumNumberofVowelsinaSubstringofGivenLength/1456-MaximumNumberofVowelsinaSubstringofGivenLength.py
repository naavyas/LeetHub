# Last updated: 5/16/2025, 11:10:08 PM
"""
return the max number vowels 
fixed length of substring given as k 
vowels : a e i o u
input: s = 'abciiidef' 
k = 3
first we go through the first 3 letters 
we keep a count of the number of vowels
we also have a max_vowel variable to help us keep track of the max
we keep going from left to right and as we move we change the vowel count and only update the max variable if the new count is greater 
we then finally return the max_count variable 
"""
from collections import defaultdict
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = list()
        vowels = ['a', 'e', 'i', 'o', 'u']
        left = 0
        right = 0
        vowel_count = 0 
        max_vowel = 0
        for r in range(k): #loop to go through the fixed part of the string first
            if s[right] in vowels:
                vowel_count += 1
            right+=1
        max_vowel = max(max_vowel,vowel_count)
        right = k - 1
        while right<len(s):
            right += 1
            while left<right and right<len(s) and right-left == k:
                if s[right] in vowels:
                    vowel_count += 1
                if s[left] in vowels:
                    vowel_count -= 1
                left+= 1
            max_vowel = max(max_vowel,vowel_count)

        return max_vowel



            




        