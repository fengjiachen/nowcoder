class Solution:
    def rectCover(self, number):
        if number < 1:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            last = 1
            current = 2
            for i in range(3, number + 1):
                temp = current + last
                last = current
                current = temp
            return current
