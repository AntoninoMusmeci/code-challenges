#https://leetcode.com/problems/longest-turbulent-subarray/editorial/
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        current_sign = ""
        prev_sign = ""
        current_len = 1
        result = 1
        for i in range(1,n):
            current_sign = "<" if arr[i - 1] < arr[i] else ">" if arr[i - 1] > arr[i] else "="
            if current_sign == "=":
                current_len = 1
                continue
            if current_sign == prev_sign and prev_sign != "":
                current_len = 1
            prev_sign = current_sign
            current_len += 1
            result = max(result, current_len)
        return result