#https://leetcode.com/problems/car-fleet/description/
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for pos, s in zip(position, speed):
            cars.append((pos,s))
        cars.sort()
        fleet = []
        number_of_fleet = 0
        for i in range(len(cars)-1,-1,-1):
            p,s = cars[i]
            time = (target - p) / s
            if not fleet:
                fleet.append(time)
                continue
            if time > fleet[-1]:
                fleet.append(time) 
        return len(fleet)