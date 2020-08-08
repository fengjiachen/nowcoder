class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            p = 1
            l = 2
            for i in range(3, number+1):
                temp = p + l
                p = l
                l = temp
            return l
