class Solution:

    def __init__(self):
        self.s_in = []
        self.s_out = []

    def push(self, node):
        # write code here
        self.s_in.append(node)

    def pop(self):
        # return xx
        if len(self.s_out) == 0:
            while len(self.s_in) > 0:
                temp = self.s_in[-1]
                self.s_in.pop()
                self.s_out.append(temp)
        if len(self.s_out) != 0:
            temp = self.s_out[-1]
            self.s_out.pop()
            return temp
        else:
            return None
