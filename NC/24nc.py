class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        ret = ListNode(0)
        rear = ret
        target = head
        num = 1
        head = head.next
        while head:
            if head.val == target.val:
                num += 1
                # print('+1')
            else:
                if num == 1:
                    rear.next = target
                    rear = rear.next
                target = head
                num = 1
            head = head.next
        if num == 1:
            rear.next = target
            rear = rear.next
        rear.next = None
        return ret.next


if __name__ == '__main__':
    s = Solution()
    l = ListNode(2)
    l.next = ListNode(2)
    l.next.next = ListNode(3)

    ans = s.deleteDuplicates(l)
    while ans:
        print(ans.val)
        ans = ans.next
