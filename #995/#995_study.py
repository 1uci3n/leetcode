# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-02-18 23:52:36
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-02-19 00:32:00

# 负雪明烛 https://leetcode-cn.com/u/fuxuemingzhu/
class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        que = []
        counter = 0
        for i in range(n):
            if len(que) != 0:
                if (que[0] + K -1) < i:
                    que.pop(0)
            if (len(que) % 2) == 0:
                if A[i] == 0:
                    if i + K > n:
                        return -1
                    else:
                        que.append(i)
                        counter += 1
            else:
                if A[i] == 1:
                    if i + K > n:
                        return -1
                    else:
                        que.append(i)
                        counter += 1
        return counter