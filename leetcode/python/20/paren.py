class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair_dict = {"(": ")", "[": "]", "{": "}"}
        i = 0
        length_s = len(s)
        while i < length_s:
            if s[i] in pair_dict:
                left = s[i]
                right = pair_dict[left]
                if i != len(s) and s[i+1] == right:
                    i += 2
                else:
                    return False
            else:
                i += 1
        return True



s = Solution()
s.isValid("{[]}")