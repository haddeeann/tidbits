class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_total = 0
        max_right_i = len(height) - 1
        max_left_i = 0
        for i, x in enumerate(height[::-1]):
            marker = len(height)-i-1
            for j, y in enumerate(height[:marker]):
                length = marker - j
                bar_height = min(x, y)
                test_area = length * bar_height
                if test_area > max_total:
                    max_total = test_area

        return max_total


height = [1,8,6,2,5,4,8,3,7]
heighi = [0,1,2,3,4,5,6,7,8]
answer = 49
test = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
sol = Solution()
sol.maxArea(height)

