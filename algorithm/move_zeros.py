class Solution:
    def moveZeroes(self, nums):
        length = len(nums)
        k = 0
        for i in range(length):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range(k, length):
            nums[i] = 0
