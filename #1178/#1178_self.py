# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-02-26 23:31:06
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-02-26 23:33:47

# Time out O(MN)
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        nw = len(words)
        np = len(puzzles)
        result = []
        for i in range(np):
            temp_r = 0
            atama = puzzles[i][0]
            for j in range(nw):
                if atama in words[j]:
                    flag = 1
                    for m in range(len(words[j])):
                        if words[j][m] not in puzzles[i]:
                            flag = 0
                            break
                    if flag == 1:
                        temp_r += 1
            result.append(temp_r)
        return result