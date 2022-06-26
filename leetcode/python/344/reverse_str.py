import math
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        half = math.floor(len(s) / 2)
        right = s[half:]
        left = s[:half]

        for i, x in enumerate(s):
            if len(right) > 0:
                letter = right.pop()
            else:
                letter = left.pop()
            s[i] = letter

        print(s)


sol = Solution()
sol.reverseString(["h", "e", "l", "l", "o"])

