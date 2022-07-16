class Solution(object):
    def isMatch(self, s, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if pattern.find("*") == -1 and pattern.find(".") == -1:
            if s == pattern:
                return True
            else:
                return False

        s_i = len(s) - 1
        star = False
        star_dot = False
        star_dot_i = None
        for i, x in enumerate(pattern[::-1]):
            str_i = s[s_i]
            if star_dot:
                star_dot = False
                if x != str_i:
                    while s_i < star_dot_i and x != str_i:
                        s_i += 1
                        str_i = s[s_i]
                    if str_i != x:
                        return False

            if star:
                star = False

                if x == ".":
                    star_dot = True
                    star_dot_i = s_i
                    match = str_i
                else:
                    match = x
                letter = str_i
                while match == letter and s_i > 0:
                    s_i -= 1
                    str_i = s[s_i]
                    letter = str_i

                # if last elem of pattern and there's more string left
                if i == len(pattern) - 1 and s_i > 0:
                    return False

                continue

            if s_i < 0 and x != "*":
                return False

            if x == str_i:
                # if last elem of pattern and there's more string left
                if i == len(pattern) - 1 and s_i > 0:
                    return False
                s_i -= 1
                str_i = s[s_i]
            elif x == "*":
                star = True
            elif x == ".":
                # if last elem of pattern and there's more string left
                if i == len(pattern) - 1 and s_i > 0:
                    return False
                s_i -= 1
                str_i = s[s_i]
            else:
                s_i -= 1
                str_i = s[s_i]
                return False

        return True

m = "aa"
n = "a"
answer = False

l = "aab"
o = "c*a*b"
answer = True

p = "aa"
q = "a*"
answer = True


a = "abcd"
b = "d*"
answer = False

c = "aaa"
d = ".a"
answer = False

e = "aaa"
f = "ab*a"
answer = False

g = "a"
h = "ab*a"
answer = False

i = "ab"
j = ".*.."

aa = "aasdfasdfasdfasdfas"
bb = "aasdf.*asdf.*asdf.*asdf.*s"

cc = "aasdfasdfasdfasdfas"
dd = "aasdf.*asdf.*asdf.*asdf.*s"

ee = "ab c de de"
ff = "ab .* de"


answer = True

sol = Solution()

if sol.isMatch(cc, dd):
    print("ten test passed")
else:
    print("ten test failed")
#
# if not sol.isMatch(m, n):
#     print("first test passed")
# else:
#     print("first test failed")
#
# if sol.isMatch(l, o):
#     print("second test passed")
# else:
#     print("second test failed")
#
# if sol.isMatch(p, q):
#     print("third test passed")
# else:
#     print("third test failed")
#
# if not sol.isMatch(a, b):
#     print("fourth test passed")
# else:
#     print("fourth test failed")
#
# if not sol.isMatch(c, d):
#     print("fifth test passed")
# else:
#     print("fifth test failed")
#
# if not sol.isMatch(e, f):
#     print("sixth test passed")
# else:
#     print("sixth test failed")
#
# if not sol.isMatch(g, h):
#     print("seven test passed")
# else:
#     print("seven test failed")
#
# if sol.isMatch(i, j):
#     print("eight test passed")
# else:
#     print("eight test failed")
#
# if sol.isMatch(aa, bb):
#     print("ninth test passed")
# else:
#     print("ninth test failed")