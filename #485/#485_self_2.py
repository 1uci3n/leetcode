# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-02-15 14:46:33
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-02-15 14:49:04
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        current_num = 0
        for i in nums:
            if i == 1:
                current_num += 1
            else:
                if current_num > max_num:
                    max_num = current_num
                current_num = 0
        if current_num > max_num:
            max_num = current_num
        return max_num