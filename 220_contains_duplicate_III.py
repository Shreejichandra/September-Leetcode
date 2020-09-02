'''Given an array of integers, find out whether there are two distinct indices i and j in the array such that 
the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        l = []
        for i, j in enumerate(nums):
            l.append((j, i))
            
        l.sort(key = lambda x: x[0])
        #print(l)
        i = 0
        j = 1
        while j < n:
            if abs(l[j][0] - l[i][0]) <= t and abs(l[j][1] - l[i][1]) <= k:
                return True
            if abs(l[j][0] - l[i][0]) > t:
                i += 1
                j = i + 1
            elif abs(l[j][0] - l[i][0]) <= t and abs(l[j][1] - l[i][1]) > k:
                j += 1
        return False
            
        
