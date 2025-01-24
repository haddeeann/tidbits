class Solution(object):
    def checkLongest(self, a, b):
        if len(a) >= len(b):
            return a
        else:
            return b

    def testPally(self, left, right, base, longest):
        longest = self.checkLongest(longest, base)
        min_length = min(len(left), len(right))
        if len(right) > min_length:
            right = right[:min_length]
        elif len(left) > min_length:
            left = left[-min_length:]
        if left and right and left == right:
            pally = left + base + right
            longest = self.checkLongest(longest, pally)
        return longest

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        for index, letter in enumerate(s):
            if index > 0:
                a = s[index - 1]
                if a == letter:
                    longest = self.testPally(left=s[:index - 1], right=s[index + 1:], base=a + letter, longest=longest)

            longest = self.testPally(left=s[:index], right=s[index + 1:], base=letter, longest=longest)

        return longest