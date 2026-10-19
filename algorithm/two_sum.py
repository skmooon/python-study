"""LeetCode HOT 100 第 1 题：两数之和。

题目：https://leetcode.cn/problems/two-sum/
接收整数列表 nums 和目标值 target，返回和为 target 的两个元素下标。
同一个元素不能使用两次；题目保证恰好一组答案，下标顺序不限。
今天先自己写双循环版本，暂不要求字典优化，不修改原列表。
返回的是下标列表，不是两个元素的值，也不是打印结果。
文件不放示例或测试代码，写完由助手在文件外验收。
"""


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
