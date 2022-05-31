class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        end = len(nums) - 1
        if target <= nums[0]:
            return 0
        elif target > nums[end]:
            return len(nums)

        for i, x in enumerate(nums[:-1]):
            if target == nums[i]:
                return i
            elif target <= nums[i+1]:
                return i + 1


arr = [1, 3]
target = 3
output = 1
sol = Solution()

answer = sol.searchInsert(arr, target)
if output == answer:
    print("answer is found", answer)