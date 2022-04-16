import math


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # find the longest possible pal
        # for each letter
        for i, letter in enumerate(s[1:], start=1):
            # find the possible substrings
            end_index = len(s) - 1
            # single letter combo
            if i != end_index:
                right = end_index - i
                left = i
                length = right if right <= left else left
                substring = s[i - length: i + length + 1]
                print("single: ", substring)
            # double letter combo
            if s[i - 1] == s[i]:
                combo = s[i - 1] + s[i]
                if i != 1 and i != end_index:
                    right = end_index - i
                    left = i - 1
                    length = right if right <= left else left
                    left_start = i - length - 1
                    right_end = i + length + 1
                    left_substring = s[left_start: i - 1]
                    right_substring = s[i + 1: right_end]
                    substring = left_substring + combo + right_substring
                    print("combo: ", substring)
                else:
                    print("combo: ", combo)


sol = Solution()
sol.longestPalindrome("aacceff")