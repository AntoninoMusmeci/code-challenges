# https://leetcode.com/problems/continuous-subarray-sum/description/
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminders = {0: -1}
        # the 0:-1 is added because the subArray can start at position 0
        numbers_sum = 0
        for i in range(len(nums)):
            numbers_sum += nums[i]
            reminder = numbers_sum % k
            """ if the same reminder is found 2 times
            nums = [23,2,4,6,7]
            23 % 6 = 5
            (23 + 2 + 4) % 6 = 5
            it means that there is a multiple of k beetween the 2 numbers
            """
            if reminder in reminders:
                if i - reminders[reminder] >= 2:
                    return True
            else:
                reminders[reminder] = i
        return False
