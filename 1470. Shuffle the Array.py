#https://leetcode.com/problems/shuffle-the-array/description/
class Solution:
    def shuffle(self, nums, n):
        for i in range(n, n * 2):
            num = nums[i] << 10  #num[i] + [0]*10
            nums[i- n] |= num # 2bit + 10bit + 10bit = 2bit + y + x
        tenOnes = int(pow(2, 10)) - 1
        for i in range(n-1,-1,-1): #start from the center of the array and go backward
            y = nums[i] >> 10 
            x = nums[i] & tenOnes #--yx & 000000000..1111111111 =  ...x
            nums[2 * i + 1] = y
            nums[2 * i] = x
        return nums