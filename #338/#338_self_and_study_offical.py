# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-03-03 15:04:22
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-03-03 19:05:49
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]
        for i in range(1, num + 1):
            if (i - 1)&i == 0:
                max_bit = i
            result.append(result[i - max_bit] + 1)
        return result