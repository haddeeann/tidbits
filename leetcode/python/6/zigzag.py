class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr = []
        for row in range(numRows):
            arr.append([])
        print(arr)
        arr[0].append(s[0])
        arr[0].append(s[1])
        arr[0].append(s[2])
        arr[0].append(s[3])
        arr[0].append(s[4])
        print(arr)


sol = Solution()
sol.convert("stringsaregood", 5)