class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr = []
        arr.append([])
        for x in range(numRows):
            arr[0].append('')
        arr[0][0] = s[0]
        arr[0][1] = s[1]
        arr[0][2] = s[2]
        arr[0][3] = s[3]
        arr[0][4] = s[4]

        arr.append([])
        for x in range(numRows):
            arr[1].append('')
        arr[1][3] = s[5]

        arr.append([])
        for x in range(numRows):
            arr[2].append('')
        arr[2][2] = s[6]

        arr.append([])
        for x in range(numRows):
            arr[3].append('')
        arr[3][1] = s[7]

        arr.append([])
        for x in range(numRows):
            arr[4].append('')
        arr[4][0] = s[8]
        arr[4][1] = s[9]
        arr[4][2] = s[10]
        arr[4][3] = s[11]
        arr[4][4] = s[12]

        arr.append([])
        for x in range(numRows):
            arr[5].append('')
        print(arr)


sol = Solution()
sol.convert("stringsaregoodandtheyarelong", 5)