# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-02-18 22:19:07
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-02-18 23:52:59
class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
    # Time out cause O(N*K)
        counter = 0
        for i in range(len(A) - K + 1):
            if A[i] == 0:
                for j in range(K):
                    A[i + j] = inv(A[i + j])
                counter += 1
        for i in range(1, K + 1):
            if A[-i] == 0:
                return -1
        return counter

    def inv(num):
        if num == 0:
            return 1
        else:
            return 0
