'''You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. '''


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        people = [0] * 1000
        for i in trips:
            people[i[1]] += i[0]
            people[i[2]] -= i[0]
            
        count = 0
        #print(people)
        for j in people:
            count += j
            if count > capacity:
                return False
        return True
        
        
        
       #NAIVE APPROACH O(N^2) 
        
        # people = [0] * 1001
        # for i in trips:
        #     start = i[1]
        #     end = i[2]
        #     for j in range(start, end):
        #         people[j+1] += i[0]
        # # print(people)
        # # print(max(people))
        # return max(people) <= capacity
