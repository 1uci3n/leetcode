# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-02-25 23:43:45
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-02-25 23:44:06
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        if m == n:
            size = m
            for level in range(size):
                i = level
                for j in range(level, size):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
            return matrix
        else:
            result = []
            for i in range(n):
                temp = []
                for j in range(m):
                    temp.append(matrix[j][i])
                result.append(temp)
            return result