# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if len(self.min_stack) == 0:
            self.min_stack.append(node)
        else:
            temp = self.min_stack[-1]
            if node <= temp:
                self.min_stack.append(node)
            else:
                self.min_stack.append(temp)

    def pop(self):
        # write code here
        if len(self.stack) > 0:
            self.min_stack.pop()
            self.stack.pop()

    def top(self):
        # write code here
        if len(self.stack) > 0:
            return self.stack[-1]

    def min(self):
        # write code here
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
