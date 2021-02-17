# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-02-17 00:04:36
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-02-17 00:54:18
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        # a = [nums[0]]
        # for i in range(1, len(nums)):
        #     if nums[i] <= a[0]:
        #         a.insert(0, nums[i])
        #         continue
        #     for j in range(0, len(a) - 1):
        #         if (nums[i] > a[j]) & (nums[i] <= a[j + 1]):
        #             a.insert(j+1, nums[i])
        #             break
        #     if nums[i] > a[-1]:
        #         a.insert(len(a), nums[i])
        sums = 0
        a = sorted(nums)
        for i in range(n):
            sums += a[i * 2]
        return sums