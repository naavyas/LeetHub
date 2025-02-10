"""
Logic - push all the numbers as you iterate through the string 
Once you see a operator start popping the numbers and doing the operations
thinking of valid examples:

"""
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        operators = ['+', '-', '*', '/']
        output = 0
        flag = False
        for r in range(len(tokens)):
            if tokens[r] in operators:
                if len(stack)!=0:
                    val = stack.pop()
                    output = int(val)
                    #print('output after popping when its the first: ', output)
                    val = stack.pop()
                    if tokens[r] == '+':
                        output = int(val) + output 
                    if tokens[r] == '-':
                        output = int(val) - output
                    if tokens[r] == '*':
                        output = int(val) * output
                    if tokens[r] == '/':
                        output = int(int(val) / output)
                    #print('output after first: ', output)
                    stack.append(output)

            else:
                stack.append(tokens[r])
                #print('stack after pushing: ', stack)
        #print('final output: ', output)
                    
        
        return output





        