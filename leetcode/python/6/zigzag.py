class Solution(object):
    def fill(self, numRows, arr):
        col = len(arr)
        arr.append([])
        for x in range(numRows):
            arr[col].append('')

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # set up once
        arr = []
        z = 0

        # pattern one
        self.fill(numRows, arr)
        y = 0
        while y < numRows:
            arr[0][y] = s[z]
            y += 1
            z += 1

        # pattern two
        i = 1
        j = 3
        while j > 0:
            self.fill(numRows, arr)
            arr[i][j] = s[z]
            i += 1
            j -= 1
            z += 1

        # pattern one
        self.fill(numRows, arr)
        y = 0
        while y < numRows:
            arr[4][y] = s[z]
            y += 1
            z += 1

        # pattern two
        i = 5
        j = 3
        while j > 0:
            self.fill(numRows, arr)
            arr[i][j] = s[z]
            i += 1
            j -= 1
            z += 1

        # pattern one
        self.fill(numRows, arr)
        y = 0
        while y < numRows:
            arr[8][y] = s[z]
            y += 1
            z += 1

        print(arr)


sol = Solution()
sol.convert("stringsaregoodandtheyarelongstringsaregoodandtheyarelong", 5)