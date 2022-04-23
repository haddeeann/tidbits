class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        rev_ans = 0
        hex_lower = -0x80000000
        hex_upper = 0x7fffffff

        if x < 0:
            rev_str_x = "-" + str_x[:0:-1]
            rev_int = int(rev_str_x)
        else:
            rev_str_x = str_x[::-1]
            rev_int = int(rev_str_x)

        if x >= 0:
            if rev_int == rev_int & hex_upper:
                rev_ans = rev_int
        else:
            if hex_lower == rev_int & hex_lower:
                rev_ans = rev_int
        return rev_ans


sol = Solution()
sol.reverse(-123)