# Last updated: 4/1/2025, 11:04:09 AM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #first we sort all the inputs based on on the first value
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key = lambda x: x[0])
        #[1,3],[2,6],[8,10],[15,18]]
        #[[1,6]]
        #pointer = 1
        queue = []
        pointer = 0
        queue.append(intervals[pointer])
        pointer += 1
        while pointer<len(intervals):
            var = queue[-1]
            if var[1]>=intervals[pointer][0]:
                var = queue.pop(-1)
                max_end_val = max(var[1],intervals[pointer][1])
                queue.append([var[0],max_end_val])
            else:
                queue.append(intervals[pointer])
            pointer += 1
            
        return queue
        