#https://leetcode.com/problems/kth-missing-positive-number/editorial/
class Solution:      
        def findKthPositive(self, arr: List[int], k: int) -> int:
            left, right = 0, len(arr) - 1
            while left <= right:
                m = (left + right) // 2
                if arr[m] - m - 1 < k:
                    left = m + 1
                else:
                    right = m - 1
            return left + k