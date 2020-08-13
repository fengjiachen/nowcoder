class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        head = None
        while pHead != None:
            temp = pHead
            pHead = pHead.next
            temp.next = head
            head = temp
        return head
