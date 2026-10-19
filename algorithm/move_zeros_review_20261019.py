"""2026 年 10 月 19 日独立复写：LeetCode 283 移动零。

原题：https://leetcode.cn/problems/move-zeroes/
将所有零移动到列表末尾，保持非零元素相对顺序。
原地修改 nums，不复制列表，额外空间 O(1)，返回 None。
先不看昨天的 move_zeros.py；有提示时如实记录，不计为完全独立。
此文件只留题目和方法位置，不包含示例或测试代码。
"""


class Solution:
    def moveZeroes(self, nums):
        k = 0
        if nums == []:
            return None
        for i in nums:
            if i != 0:
                nums[k] = i
                k += 1
        for i in range(k, len(nums)):
            nums[i] = 0
