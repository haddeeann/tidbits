class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        for x in range(zeros):
            nums.remove(0)

        for x in range(zeros):
            nums.append(0)

        print(nums)


sol = Solution()
nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)
