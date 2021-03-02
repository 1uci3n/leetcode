# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-03-02 18:01:13
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-03-02 18:34:55
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sum_matrix = []
        for i in range(len(matrix)):
            temp = []
            temp_sum = 0
            for j in range(len(matrix[0])):
                temp.append(temp_sum)
                temp_sum += matrix[i][j]
            self.sum_matrix.append(temp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        reslut = 0
        for i in range(row1, row2 + 1):
            reslut += self.sum_matrix[i][col2] - self.sum_matrix[i][col1] + self.matrix[i][col2]
        return reslut


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)