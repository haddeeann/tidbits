class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def kSum(nums, target, k):
            res = []

            if not nums:
                return res

            average_value = target // k

            if average_value < nums[0] or nums[-1] < average_value:
                return res

            if k == 2:
                return twoSum(nums, target)

            for i, value in enumerate(nums):
                # if it's the first value or if it's not a repeat
                if i == 0 or nums[i - 1] != value:
                    for subset in kSum(nums[i + 1:], target - value, k - 1):
                        print(subset)
                        res.append([value] + subset)

            return res

        def twoSum(nums, target):
            res = []
            lo, hi = 0, len(nums) - 1

            while lo < hi:
                curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

            return res

        nums.sort()
        return kSum(nums, target, 4)

sol = Solution()
sol.fourSum([1,0,-1,0,-2,2], 0)