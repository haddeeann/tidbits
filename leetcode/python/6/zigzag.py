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
                if z == s_length:
                    break
                arr[i][y] = s[z]
                y += 1
                z += 1

            # pattern two
            i += 1
            j = numRows - 2
            while j > 0:
                if z == s_length:
                    break
                self.fill(numRows, arr)
                arr[i][j] = s[z]
                i += 1
                j -= 1
                z += 1

        row = 0
        build_string = ''
        while row < numRows:
            col = 0
            while col < len(arr):
                if arr[col][row] != '':
                    build_string += arr[col][row]
                col += 1
            row += 1

        return build_string


sol = Solution()
sol.convert("PAYPALISHIRING", 3)