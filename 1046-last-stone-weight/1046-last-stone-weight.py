"""
Understand : 
After every iteration we then have to remove the smaller (destroyed stone) element from the array? Or based on the space complexity we can create a new array each time and recursively pass it to the fucntion? 
The input is the array with all the stones and the int weight of the final stone left after the whole game is complete 
What is the space and time complexity to be followed? 
Can the array contain 0 or negative numbers

Match / Plan: 
Lets go through all the options - 
1. We have a for loop with two variables that help keep track of the first max and the second max. 
2. Then we using if - else conditions we go through the conditions of destroying one stone and putting the remaining weight of the stone in the array. 
3. Maybe we can also use recursion by creating a seperate method to find the two max stones 
"""

class Solution:
    def max_val(self, stones):
        max_s = stones[0]
        max_s1 = float('-inf')
        for i in stones:
            if i > max_s:
                max_s1 = max_s
                max_s = i
            elif i > max_s1 and i != max_s:
                max_s1 = i
        return max_s, max_s1
    
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort(reverse=True)  # Ensure the stones are sorted so the two largest are always at the start
            num1 = stones.pop(0)  # Remove the largest stone
            num2 = stones.pop(0)  # Remove the second largest stone
            if num1 != num2:  # If they are not the same, the remainder goes back to the list
                stones.append(num1 - num2)  # Append the difference

        return stones[0] if stones else 0 