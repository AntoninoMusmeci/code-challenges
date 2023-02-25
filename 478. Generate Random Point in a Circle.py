import random
import math
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius * radius
        self.x_start = x_center - radius
        self.x_center = x_center
        self.x_end = x_center + radius
        self.y_center = y_center

    def randPoint(self):
        x = random.uniform(self.x_start, self.x_end)
        y = math.sqrt(self.radius - (x - self.x_center) ** 2)
        y_end = y + self.y_center
        y_start = self.y_center - y
        y = random.uniform(y_start, y_end)
        
        return [x,y]
    
# s = Solution(0.01,-73839.1,-3289891.3)
# i= 0
# x_p = 0
# y_p = 0
# while i < 30000001:
#     i+= 1
#     x,y = s.randPoint()


#     if x > -73839.1:
#         x_p = x_p + 1
        
       
#     if y <-3289891.3:
#         y_p += 1
    
# print(x_p, y_p)