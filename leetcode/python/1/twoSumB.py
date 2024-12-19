class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for index, value in enumerate(nums):
            complementary = target - value
            if complementary in num_to_index:
                return [num_to_index[complementary], index]
            num_to_index[value] = index

sol = Solution()
answer = sol.twoSum([1,3,1,1,3], 6)
print(answer)
