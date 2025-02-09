"""
given : array of citations
Each element is the number of citations a researcher recieves for their ith paper 
the number of paper published : h (i.e h occurrences of the researcher representing the number of papers published 
Number of times each paper has been cited is h )

Looking at the example I can see that we we have to take create a dictionary to store the max number of papers that have value of the citations greater than or equal to itself and then return that `
Two approaches that come to mind: 
Using a dict that stores the number of papers as the key and the count of the that are greater than equal to that key as the value 
IMP keyword to remeber is at Least and so the max value that is returned will just be the key of the dict 
- maybe i should sort the array that way and i can reduce using an extra loop
so the array will then look like:
[3,0,6,1,5]
[0,1,3,5,6]

[1,3,1]
[1,1,3]

Test cases: 
[0,1,7,8,9]

[0,0,0]
"""
from collections import defaultdict
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        citations = sorted(citations) 
        for r in range(len(citations)):
            if citations[r]<=len(citations)-r:
                h_index = citations[r]
            else:
                if citations[r]>=len(citations)-r:
                    index = len(citations)-r
                    h_index = max(index,h_index)

        return h_index
                













        