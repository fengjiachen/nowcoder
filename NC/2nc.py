class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head):
        if head == None:
            return None
        li = []
        while head:
            li.append(head)
            head = head.next
        head = li.pop(0)
        index = head
        while len(li) > 0:
            index.next = li.pop()
            index = index.next
            if len(li) > 0:
                index.next = li.pop(0)
                index = index.next
        index.next = None
        return head
