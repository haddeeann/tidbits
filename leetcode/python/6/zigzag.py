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
        i = 0

        s_length = len(s)

        while z < s_length:
            # pattern one
            self.fill(numRows, arr)
            y = 0
            while y < numRows:
                arr[i][y] = s[z]
                y += 1
                z += 1

            # pattern two
            i += 1
            j = 3
            while j > 0:
                self.fill(numRows, arr)
                arr[i][j] = s[z]
                i += 1
                j -= 1
                z += 1

        for index, a in enumerate(arr):
            print(a)


sol = Solution()
sol.convert("stringsaregoodandtheyarelongstringsaregoodandtheyarelong", 5)