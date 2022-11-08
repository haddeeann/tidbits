class Solution(object):
    def divide(self, x, y):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans = 0
        min = -2**31
        max = 2**31-1
        xx, yy = abs(x), abs(y)
        for i in range(32, -1, -1):
            if xx >= (yy << i):
                subtract = (yy << i)
                xx -= subtract
                add = (1 << i)
                ans += add

        x_neg = x < 0
        y_neg = y < 0
        if (x_neg and not y_neg) or (y_neg and not x_neg):
            ans = -ans

        if ans < min:
            return min
        elif ans > max:
            return max

        return ans


sol = Solution()

sol.divide(112, 3)