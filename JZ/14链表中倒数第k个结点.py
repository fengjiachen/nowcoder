class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        count = 0
        previsou = head
        current = head
        while current != None:
            if count >= k:
                previsou = previsou.next
            current = current.next
            count += 1
        if count < k:
            return None
        else:
            return previsou
