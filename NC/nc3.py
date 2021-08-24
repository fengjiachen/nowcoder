# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead == None or pHead.next == None:
            return None
        slow = fast = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = pHead
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast
        return None


def main():
    l = ListNode(1)
    l = [ListNode(i) for i in range(1, 6)]
    for i in range(4):
        l[i].next = l[i + 1]
    l[4].next = l[2]

    s = Solution()
    t = s.EntryNodeOfLoop(l[0])
    if t:
        print(t.val)
    else:
        print(t)


if __name__ == '__main__':
    main()
