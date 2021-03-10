# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-03-10 16:02:41
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-03-10 16:03:13
class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        kuohao = []
        temp_sums = []
        temp_sum = 0
        temp_str = '0'
        while i < len(s):
            if s[i] == ' ':
                s = s[:i] + s[i + 1:]
                continue
            else:
                if s[i] == '(':
                    temp_sum += int(temp_str)
                    temp_str = '0'
                    temp_sums.append(temp_sum)
                    temp_sum = 0
                    if i == 0:
                        kuohao.append(1)
                    else:
                        if s[i - 1] == "-":
                            kuohao.append(-1)
                        else:
                            kuohao.append(1)
                elif s[i] == ')':
                    temp_sum += int(temp_str)
                    temp_str = '0'
                    temp_sum = temp_sums.pop(-1) + (temp_sum * kuohao.pop(-1))
                elif (s[i] == '+') or (s[i] == '-'):
                    temp_sum += int(temp_str)
                    temp_str = '0'
                else:
                    if i == 0:
                        temp_str = s[i]
                    else:
                        if (s[i - 1] == '(') or (s[i - 1] == ")"):
                            temp_str = s[i]
                        elif s[i - 1] == '+':
                            temp_str = s[i]
                        elif s[i - 1] == '-':
                            temp_str = s[i-1:i+1]
                        else:
                            temp_str += s[i]
                i += 1
        temp_sum += int(temp_str)
        return temp_sum