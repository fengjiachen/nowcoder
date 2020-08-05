class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        l = len(s)
        num_space = [0] * l
        current_num = 0
        for i in range(l):
            if s[i] == ' ':
                current_num += 1
            num_space[i] = current_num
        new_char_list = [' '] * (l + current_num * 2)
        i = l - 1
        j = l+current_num*2-1
        while i >= 0:
            if s[i] != ' ':
                new_char_list[j] = s[i]
                j -= 1
            else:
                new_char_list[j] = '0'
                new_char_list[j-1] = '2'
                new_char_list[j - 2] = '%'
                j -= 3
            i -= 1
        return ''.join(new_char_list)


if __name__ == "__main__":
    h = 'hello world'
    s = Solution()
    print(s.replaceSpace(h))
