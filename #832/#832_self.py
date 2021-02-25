# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-02-25 14:03:19
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-02-25 14:03:34
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if (len(A[0]) % 2) == 0:
            itzi = len(A[0]) // 2
        else:
            itzi = (len(A[0]) // 2) + 1
        for i in range(len(A)):
            for j in range(itzi):
                temp = invn(A[i][j])
                A[i][j] = invn(A[i][-(j + 1)])
                A[i][-(j + 1)] = temp
        return A

def invn(a: int) -> int:
    if a != 0:
        return 0
    else:
        return 1