class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类
#
class Solution:
    def reverseBetween(self, head, m, n):
        vhead = ListNode(0)
        vhead.next = head
        pre = vhead
        start = end = head
        for i in range(m - 1):
            pre = pre.next
            start = start.next
        for i in range(n - 1):
            end = end.next
        while start != end:
            pre.next = start.next
            start.next = end.next
            end.next = start
            start = pre.next
        return vhead.next

    def reverseN(self, head, n):
        if n == 1:
            self.seccussor = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.seccussor
        return last

    def reverseBetween2(self, head, m, n):
        self.seccussor = None
        if m == 1:
            return self.reverseN(head, n)
        head.next = self.reverseBetween2(head.next, m - 1, n - 1)
        return head
