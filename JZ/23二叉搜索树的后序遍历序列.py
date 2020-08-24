class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == None or len(sequence) == 0:
            return False
        l = len(sequence)
        if l == 1:
            return True
        split = 0
        while split < l and sequence[split] < sequence[-1]:
            split += 1
        temp = split
        while temp < l-1:
            if sequence[temp] < sequence[-1]:
                return False
            temp += 1
        left = True
        if split > 0:
            left = self.VerifySquenceOfBST(sequence[:split])
        right = True
        if split < l-1:
            right = self.VerifySquenceOfBST(sequence[split:-1])
        return left and right


if __name__ == "__main__":
    s = Solution()
    print(s.VerifySquenceOfBST([]))
