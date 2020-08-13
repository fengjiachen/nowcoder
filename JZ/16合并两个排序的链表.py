class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        head = ListNode(1)
        current = head
        while pHead1 != None and pHead2 != None:
            if pHead1.val < pHead2.val:
                current.next = pHead1
                pHead1 = pHead1.next
            else:
                current.next = pHead2
                pHead2 = pHead2.next
            current = current.next
        if pHead1 != None:
            current.next = pHead1
        else:
            current.next = pHead2
        return head.next
