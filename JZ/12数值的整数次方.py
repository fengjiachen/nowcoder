class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent < 0:
            return 1/self.Power(base, abs(exponent))
        if base == 0:
            return 0
        elif exponent == 0:
            return 1
        elif exponent == 1:
            return base
        if exponent % 2 == 1:
            return base * self.Power(base * base, exponent // 2)
        else:
            return self.Power(base * base, exponent // 2)
