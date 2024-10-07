# class Solution:
#     def reverse(self, x: int) -> int:
        
#         isNegative = False
#         if x < 0:
#             x = abs(x)
#             isNegative = True
        
#         result = 0
#         MAX = 2 **31 - 1
#         while x:
            
#             digit = x % 10
#             x = x // 10
            
#             if isNegative == False:
#                 if (MAX-digit-1) // 10  < result:
#                     return 0
#                 else:
#                     result = result * 10
#                     if (MAX - 1) - result < digit:
#                         return 0
#             else:
#                 if (MAX-digit) // 10  < result:
#                     return 0
#                 else:
#                     result = result * 10
#                 if (MAX) - result < digit:
#                         return 0
#             result += digit
        
#         result = -result if isNegative else result
#         return result
# sol = Solution()

# print(sol.reverse(6463847412))


class Matrix:
    M = [[0,0],[1,1]]
    def dimensions(self):
        return [2,2]
    def get(self,r,c):
        return self.M[r][c]

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix) -> int:
        
        R,C = binaryMatrix.dimensions()
        res = C
        found = False
        for i in range(R):
            l = 0
            r = res
            while l <= r:
                m = ( l + r ) // 2
                if binaryMatrix.get(i,m) == 0:
                    l = m + 1
                else:
                    r = m - 1
                    found = True
                    res = min(res,m)
            
        return res if found else -1

sol = Solution()
sol.leftMostColumnWithOne(Matrix())