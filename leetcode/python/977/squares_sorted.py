class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sort_list = []
        for i, x in enumerate(nums):
            squared = x * x
            sort_list.insert(i, squared)
        sort_list.sort()
        return sort_list


num = [-4, -1, 0, 3, 10]
num2 = [-7, -3, 2, 3, 11]
sol = Solution()
print(sol.sortedSquares(num))