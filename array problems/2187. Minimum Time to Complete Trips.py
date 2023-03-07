#https://leetcode.com/problems/minimum-time-to-complete-trips/description/
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        faster_bus = min(time)
        #time spentif we consider only the faster bus
        only_faster_bus = faster_bus * totalTrips

        #can we do better? binary search
        l = faster_bus
        r = only_faster_bus
        while l < r:
            #let's try half time
            m = (r - l) //2 + l
            total_trips_in_m = 0
            for t in time:
                #how many trips can bus t do in time m?
                total_trips_in_m += m // t
            if total_trips_in_m >= totalTrips:
                #try in less time
                r = m
            else:
                #try with more time
                l = m + 1
        return r