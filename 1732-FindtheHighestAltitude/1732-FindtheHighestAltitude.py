# Last updated: 3/28/2025, 11:19:32 AM
"""
understanding : 
the trip consists of n+1 points at diff altitudes
starts : point 0 
altitude = 0 
int array gain of length n 
any element in gain is the net gain between that point and the point after
algo:
have two pointers one in gains and one in output 
start with 0 and the first element 
then take the first i=1 elements from the list and add to the last element of output -- put this as 3rd element 
append this added value to the output 
then take the max value of output and return it 

"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        if len(gain) == 1:
            return max(0,gain[0])
        altitude = []
        altitude.append(0)
        altitude.append(gain[0])
        netAltitude = 1 #pointer for array altitude
        netGain = 1 #pointer for array gain
        while netGain<len(gain):
            altitude.append(gain[netGain] + altitude[netAltitude])
            netGain += 1
            netAltitude += 1
        return max(altitude)






        