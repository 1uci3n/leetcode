# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-03-05 13:57:59
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-03-05 13:58:37
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.n2 = []
        self.n2_flag = True

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.n2_flag:
            for i in range(len(self.n2)):
                self.nums.append(self.n2.pop(-1))
        self.nums.append(x)
        self.n2_flag = False
        return None

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.n2_flag:
            for i in range(len(self.nums)):
                self.n2.append(self.nums.pop(-1))
            self.n2_flag = True
        return self.n2.pop(-1)

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.n2_flag:
            for i in range(len(self.nums)):
                self.n2.append(self.nums.pop(-1))
            self.n2_flag = True
        return self.n2[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.n2_flag:
            return len(self.n2) == 0
        else:
            return len(self.nums) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()