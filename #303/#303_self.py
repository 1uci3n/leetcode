# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-03-01 15:05:02
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-03-01 15:06:22

# Time O(n)
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        result = 0
        for m in range(i, j + 1):
            result += self.nums[m]
        return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)