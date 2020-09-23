'''There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if n == 1 and gas[0] >= cost[0]:
            return 0
            
        for i in range(n):
            if gas[i] < cost[i]:
                continue
            else:
                start_idx = i
                end_idx = (i + 1) % n
                j = i
                cost_ = gas[j]
                while start_idx != end_idx:
                    cost_ =  cost_ - cost[j] + gas[end_idx]
                    if cost_ < cost[end_idx]:
                        break
                    else:
                        end_idx = (end_idx+1)%n
                        j = (j+1) % n
                        if start_idx == end_idx:
                            return start_idx
        return -1
