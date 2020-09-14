'''Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for indx, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)
                
            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                return res+intervals[indx:]
            
            else: 
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
                
        res.append(newInterval)
        return res

