# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-10-07 17:59:35
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-10-07 17:59:55

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        ints = [x % 10]
        x = x // 10
        while x > 0:
            ints.append(x % 10)
            x = x // 10
        if (len(ints) % 2) == 0:
            for i in range(len(ints) // 2):
                if ints[i] != ints[-i-1]:
                    return False            
        else:
            for i in range((len(ints) - 1) // 2):
                if ints[i] != ints[-i-1]:
                    return False
        return True