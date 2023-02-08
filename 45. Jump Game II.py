class Solution:
    def jump(self, nums: List[int]) -> int:
        distances = [0] * len(nums)
        for i in range(len(nums) - 2,-1,-1):
            if nums[i] == 0:
                distances[i] = 1001
            else:
                a = distances[i+1::i+nums[i]]
                distances[i] = 1 + min(distances[i+1:i+nums[i] + 1])
        
        return distances[0]