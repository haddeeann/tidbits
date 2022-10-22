class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = {
            "(": 0,
            "[": 0,
            "{": 0
        }

        close = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        i = 0
        length_s = len(s)
        while i < length_s:
            c = s[i]
            if c in open:
                open[c] += 1
            elif c in close:
                o = close[c]
                open[o] -= 1
            for t in open:
                if open[t] < 0:
                    return False
            i += 1
        return True



s = Solution()
test_1 = "([)]"
test_2 = "{[]}"
if not s.isValid(test_1):
    print("test passed")
else:
    print("test failed")