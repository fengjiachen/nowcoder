class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param head ListNode类
# @param x int整型
# @return ListNode类
#
class Solution:
    def partition(self, head, x):
        smallPre = ListNode(0)
        smallTail = smallPre
        largePre = ListNode(0)
        largeTail = largePre
        while head:
            if head.val < x:
                smallTail.next = head
                head = head.next
                smallTail = smallTail.next
                smallTail.next = None
            else:
                largeTail.next = head
                head = head.next
                largeTail = largeTail.next
                largeTail.next = None
        smallTail.next = largePre.next
        return smallPre.next
