class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x_idx, x in enumerate(nums[:-1]):
            for y_idx, y in enumerate(nums[x_idx + 1:], start=x_idx + 1):
                if x + y == target:
                    return [x_idx, y_idx]


sol = Solution()

print(sol.twoSum([2, 11, 1111, 115, 7], 9))
