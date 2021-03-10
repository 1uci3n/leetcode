# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-03-09 14:04:54
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-03-09 16:15:18
class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 1
        while (i < len(S)) and (len(S) > 1):
            if S[i-1] == S[i]:
                S = S[0:i - 1] + S[i + 1:]
                if i > 1:
                    i -= 1
            else:
                i += 1
        return S