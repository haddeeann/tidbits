import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        start = 0
        end = len(str_x) - 1
        midpoint = math.floor(len(str_x) / 2)
        while start < midpoint:
            if str_x[start] != str_x[end]:
                return False
            start += 1
            end -= 1

        return True


sol = Solution()
print(sol.isPalindrome(-123321))