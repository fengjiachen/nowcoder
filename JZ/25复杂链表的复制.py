class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        new_head = None
        if pHead == None:
            return new_head
        i = pHead
        d = {}
        while i != None:
            d[i.label] = RandomListNode(i.label)
            i = i.next

        new_head = d[pHead.label]
        temp_new = new_head
        while pHead:
            if pHead.next:
                temp_new.next = d[pHead.next.label]
            if pHead.random:
                temp_new.random = d[pHead.random.label]
            pHead = pHead.next
            temp_new = temp_new.next
        return new_head
