"""2026-10-23 复习：LeetCode 1 两数之和。

原题：https://leetcode.cn/problems/two-sum/
返回 nums 中相加等于 target 的两个不同下标；题目保证唯一答案。
不修改输入，返回下标列表，下标顺序不限。
关闭旧解，先独立复写双循环；今天不要求字典优化。
写完说明时间、额外空间复杂度。卡住时先求提示。
"""


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
