class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        longest = 1
        for index, str in enumerate(s):
            str_dict = {}
            found = s.find(str, index + 1)
            if found != -1:
                substring = s[index:found]
            else:
                substring = s[index:]
            if len(substring) > longest:
                for x in substring:
                    if str_dict.get(x) is not None:
                        break

                    if str_dict.get(x) is None:
                        str_dict[x] = 1

                    if len(str_dict) > longest:
                        longest = len(str_dict)

        print(longest)
        return longest


sol = Solution()
sol.lengthOfLongestSubstring('pwwkew')
