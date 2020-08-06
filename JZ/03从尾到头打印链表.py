class Solution:
    def printListFromTailToHead(self, listNode):
        if listNode == None:
            return []
        return self.printListFromTailToHead(listNode.next)+[listNode.val]
