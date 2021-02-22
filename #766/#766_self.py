# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-02-22 16:49:38
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-02-22 17:08:39
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for j in range(n-1):
            target = matrix[0][j]
            for i in range(1, m):
                if j + i < n:
                    if matrix[i][j+i] != target:
                        return False
        for i in range(1, m-1):
            target = matrix[i][0]
            for j in range(1, n):
                if j + i < m:
                    if matrix[i+j][j] != target:
                        return False
        return True