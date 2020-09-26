'''In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.'''

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        ans = duration
        n = len(timeSeries)
        for i in range(1, n):
            timestamp = timeSeries[i] - timeSeries[i-1]
            ans += duration
            if timestamp < duration:
                ans -= duration
                ans += timestamp
                
            #print(ans)
        return ans
            
            
        
