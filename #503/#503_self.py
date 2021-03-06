# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-03-06 16:01:15
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-03-06 16:01:35
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        max_point = 0
        # fix_point = 0
        search_point = 0
        result = []
        for i in range(len(nums)):
            target = nums[i]
            if i == len(nums) -1:
                search_point = 0
            else:
                search_point = i + 1
            temp_result = -1
            while search_point != i:
                if nums[search_point] > target:
                    temp_result = nums[search_point]
                    break
                if search_point == len(nums) -1:
                    search_point = 0
                else:
                    search_point += 1
            result.append(temp_result)
        return result