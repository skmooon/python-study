"""2026-10-23 复习：LeetCode 283 移动零。

原题：https://leetcode.com/problems/move-zeroes/description/
将 nums 中的零移到末尾，保持非零元素原顺序。
原地修改，不复制列表，返回 None。
关闭旧解，复写已有方法；目标 O(n) 时间、O(1) 额外空间。
重点理解写入位置与补零范围，卡住时先求提示。
"""


class Solution:
    def moveZeroes(self, nums):
        k = 0
        for i in nums:
            if i != 0:
                nums[k] = i
                k += 1
        for i in range(k, len(nums)):
            nums[i] = 0
