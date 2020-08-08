class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            ways = 1
            for i in range(2, number + 1):
                ways *= 2
            return ways
