# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-02-17 20:24:47
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-02-17 21:30:54
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        size = len(nums) * len(nums[0])
        if size == (r * c):
            n_nums = []
            for i in range(r):
                temp = []
                for j in range(c):
                    if len(nums[0]) == 0:
                        nums.pop(0)
                    temp.append(nums[0].pop(0))
                n_nums.append(temp)
            return n_nums
        else:
            return nums