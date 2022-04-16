import math


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def testLetterPalindrome(word):
            # abc
            middle = int(math.floor(len(word) / 2))
            paly_builder = word[middle]
            i_right = middle + 1
            i_left = middle - 1

            while i_left >= 0 and i_right < len(word):
                if word[i_left] != word[i_right]:
                    return paly_builder
                else:
                    paly_builder = word[i_left] + paly_builder + word[i_right]
                i_left -= 1
                i_right += 1

            return paly_builder

        def testComboPalindrome(word):
            # abcd
            middle_right = int(len(word) / 2)
            middle_left = middle_right - 1
            paly_builder = word[middle_left] + word[middle_right]
            i_right = middle_right + 1
            i_left = middle_left - 1

            while i_left >= 0 and i_right < len(word):
                if word[i_left] != word[i_right]:
                    return paly_builder
                else:
                    paly_builder = word[i_left] + paly_builder + word[i_right]
                i_left -= 1
                i_right += 1

            return paly_builder

        longest = 1
        palindrome = s[0]

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
                test_paly = testLetterPalindrome(substring)
                if len(test_paly) > longest:
                    longest = len(test_paly)
                    palindrome = test_paly

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
                    test_paly = testComboPalindrome(substring)
                    if len(test_paly) > longest:
                        longest = len(test_paly)
                        palindrome = test_paly
                else:
                    if len(combo) > longest:
                        longest = len(combo)
                        palindrome = combo

        return palindrome


sol = Solution()
sol.longestPalindrome("cccccccc")