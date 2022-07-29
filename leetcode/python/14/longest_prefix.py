class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        short = True
        count = 0
        test_value = len(strs[1]) - 1
        while short:
            for x in strs:
                print(x[count])
            count += 1
            print('hi, good looking')
            if count == test_value:
                short = False
        #["flower","flow","flight"]
        # print(strs[0][0])
        # print(strs[1][0])
        # print(strs[2][0])
        #
        # print(strs[0][1])
        # print(strs[1][1])
        # print(strs[2][1])


sol = Solution()
sol.longestCommonPrefix(["flower","flow","flight"])