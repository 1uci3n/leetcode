# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-02-21 22:26:16
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-02-22 01:43:52
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        # Forget to meet the condition of array continuity
        # 
        # nums = sorted(nums)
        # que = [nums[0]]
        # result_len = 1
        # for i in range(1, len(nums)):
        #     while (nums[i] - que[0]) > limit:
        #         que.pop(0)
        #     que.append(nums[i])
        #     temp_len = len()
        #     if temp_len > result_len:
        #         result_len = temp_len

        # return result_len
        # 
        # Time out
        # window = [nums[0]]
        # max_v = nums[0]
        # min_v = nums[0]
        # result_len = 1
        # for point in range(1, len(nums)):
        #     window.append(nums[point])
        #     if nums[point] > max_v:
        #         max_v = nums[point]
        #     elif nums[point] < min_v:
        #         min_v = nums[point]
        #     while (max_v - min_v) > limit:
        #         window.pop(0)
        #         temp_array = sorted(window)
        #         min_v = temp_array[0]
        #         max_v = temp_array[-1]
        #     temp_len = len(window)
        #     if temp_len > result_len:
        #         result_len = temp_len
        # return result_len

        window = [nums[0]]
        nums_dic = {nums[0]:1}
        sorted_nums = [nums[0]]
        max_v = nums[0]
        min_v = nums[0]
        result_len = 1
        for point in range(1, len(nums)):
            now_num = nums[point]
            if now_num in window:
                nums_dic[now_num] += 1
            else:
                nums_dic[now_num] = 1
                sorted_nums.append(now_num)
                sorted_nums = sorted(sorted_nums)
                max_v = sorted_nums[-1]
                min_v = sorted_nums[0]
            window.append(now_num)
            while (max_v - min_v) > limit:
                pop_num = window.pop(0)
                nums_dic[pop_num] -= 1
                if nums_dic[pop_num] == 0:
                    sorted_nums.remove(pop_num)
                    if pop_num == max_v:
                        if len(sorted_nums) != 0:
                            max_v = sorted_nums[-1]
                        else:
                            max_v = min_v
                    elif pop_num == min_v:
                        if len(sorted_nums) != 0:
                            min_v = sorted_nums[0]
                        else:
                            min_v = max_v
            temp_len = len(window)
            if temp_len > result_len:
                result_len = temp_len
        return result_len
