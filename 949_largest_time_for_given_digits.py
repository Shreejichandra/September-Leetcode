'''
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.
'''

from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        x = permutations(A)
        hrs_max = -1
        mins_max = -1
       
        for h1, h2, m1, m2 in x:
            hrs = h1 * 10 + h2
            mins = m1 * 10 + m2
            if 0 <= hrs < 24 and 0 <= mins < 60:
                if hrs > hrs_max:
                    hrs_max = hrs
                    mins_max = mins
                    
                elif hrs == hrs_max:
                    if mins_max < mins:
                        mins_max = mins
                        
        if hrs_max < 0:
            return ""
        return f"{hrs_max:02}:{mins_max:02}"
      
