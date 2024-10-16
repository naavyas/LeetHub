"""
UMPIRE:
Understand: reverse the intger and store it 
if on reversing the value the integer becaomes too big store in the signed int range (4 bytes) then return 0
Questions: 
Could you give me examples of cases where the return value would be 0? 
Input: int x 
Output: int x' (after it is reversed)
Match: Maybe we could use a stack to do this or maybe alternatively we can just use a while loop and %10 and multiply it with the power of 10s
Plan: 
so we start by using a while loop that uses the mod operator to extract the last term or one term at a time 
then we take a counter that is the size of the number of the digits in the number 
this counter is used to keep track of the power of 10 that we are multiplying by and keeps decrementing 
we multiply the number extracted by the mod operator with the power counter and then store that in a new variable by adding them all
"""
class Solution:
    def reverse(self, x: int) -> int:
        #two pointer appraoch 
        k = 0
        s = list(str(x))
        j = len(s)-1
        if s[0] == '-':
            k=1
        while(k<=j):
            temp = s[k]
            s[k]=s[j]
            s[j]=temp
            k+=1
            j-=1
        
        reversed_str = ''.join(s)
        x1 = int(reversed_str)
        if x1 > ((2**31)-1) or x1 < (-2**31):
            return 0
        else:
            return x1
        
    """ 
        temp = x
        temp1 = x
        sum = 0
        ctr = 0
        while(temp1!=0):
            d = temp1 % 10 
            ctr += 1
            temp1 = temp1//10
            
        while(temp!=0):
            d = temp % 10
            d = d*(10**(ctr-1))
            sum = sum+d
            ctr -= 1
            temp = temp//10
        if x>0:
            return sum
        else:
            return -1*sum
           
    
     
        s = str(x)
        stack = []
        st = ''
        if s[0]!= '-':
            for c in s:
                stack.append(c)
            for i in range(len(stack)):
                st = st + stack.pop()
        else:
            for c in s:
                while c!='-':
                    stack.append(c)
                st = '-'
            for i in range(len(stack)-1):
                st = st + stack.append(c)
        return int(st)
  """  
   
    
        