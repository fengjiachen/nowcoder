# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here

        slow = pHead
        fast = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                ans = pHead
                while ans != slow:
                    ans = ans.next
                    slow = slow.next
                return slow
