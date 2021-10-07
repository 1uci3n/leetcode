# -*- coding: utf-8 -*-
# @Author: 1uci3n
# @Date:   2021-10-07 17:22:28
# @Last Modified by:   1uci3n
# @Last Modified time: 2021-10-07 17:27:12

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        adder_val = 0
        result_head = ListNode(val=(l1.val + l2.val))
        last_node = result_head
        if last_node.val > 9:
            adder_val = 1
            last_node.val = last_node.val - 10
        while (l1.next != None) or (l2.next != None):
            if l1.next == None:
                l1.val = 0
            else:
                l1 = l1.next
            if l2.next == None:
                l2.val = 0
            else:
                l2 = l2.next
            last_node.next = ListNode(val=(l1.val + l2.val + adder_val))
            last_node = last_node.next
            adder_val = 0
            if last_node.val > 9:
                adder_val = 1
                last_node.val = last_node.val - 10
        if adder_val != 0:
            last_node.next = ListNode(val=1)
        return result_head