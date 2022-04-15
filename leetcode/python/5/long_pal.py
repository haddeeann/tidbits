class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pal = ""
        longest = 0
        if len(s) == "":
            return ""
        if len(s) == 1:
            return s
        if len(s) == 2 and s[0] != s[1]:
            return s[0]

        for i, letter in enumerate(s):
            word = letter
            lt_i = i - 1
            gt_i = i + 1
            if lt_i >= 0:
                if letter == s[lt_i]:
                    if (gt_i < len(s) and s[gt_i] != letter) or gt_i >= len(s) or (gt_i < len(s) and s[gt_i] == letter and len(s) % 2 == 0):
                        word = s[lt_i] + word
                        if len(word) > longest:
                            longest = len(word)
                            pal = word
                        lt_i -= 1

            # main loop
            while lt_i >= 0 and gt_i < len(s):
                if s[lt_i] == s[gt_i]:
                    word = s[lt_i] + word + s[gt_i]
                    lt_i -= 1
                    gt_i += 1
                    if len(word) > longest:
                        longest = len(word)
                        pal = word
                else:
                    break

        if len(s) > 0 and len(pal) == 0:
            return s[0]
        return pal


sol = Solution()
print(sol.longestPalindrome("aaaa"))
