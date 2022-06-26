class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        reversed = []
        for word in words:
            r = word[::-1]
            reversed.append(r)

        return " ".join(reversed)


sol = Solution()
print(sol.reverseWords("Let's take LeetCode contest"))