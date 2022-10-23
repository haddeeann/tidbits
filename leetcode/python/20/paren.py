class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        close = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        i = 0
        build = ""
        length_s = len(s)
        while i < length_s:
            p = s[i]
            if p not in close:
                build += p
            elif p in close:
                if len(build) == 0:
                    return False
                last_letter = build[len(build) - 1]
                if last_letter == close[p]:
                    build = build[:-1]
                else:
                    return False
            i += 1

        return len(build) == 0



s = Solution()
test_1 = "([)]"
test_2 = "{[]}"
test_3 = "["
test_4 = "]"

if not s.isValid(test_1):
    print("test passed")
else:
    print("test failed")

if s.isValid(test_2):
    print("test passed")
else:
    print("test failed")

if not s.isValid(test_3):
    print("test passed")
else:
    print("test failed")

if not s.isValid(test_4):
    print("test passed")
else:
    print("test failed")