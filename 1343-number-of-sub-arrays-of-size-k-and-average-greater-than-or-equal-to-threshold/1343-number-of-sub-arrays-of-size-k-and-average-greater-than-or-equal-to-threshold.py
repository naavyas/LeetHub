
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        window_threshold = 0 
        counter = 0
        sum_window = 0
        for i in range(k):
            sum_window += arr[i]
        window_threshold = sum_window//k
        if window_threshold>=threshold:
            counter+=1
        
        for r in range(k, len(arr)):
            sum_window += arr[r]
            sum_window-=arr[l]
            l+=1
            window_threshold = sum_window // k
            if window_threshold >= threshold:
                counter+=1
                
        return counter 
                
            
            
        