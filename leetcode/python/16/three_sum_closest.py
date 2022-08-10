class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = 0
        least_diff = None
        test_diff = 0
        nums.sort()

        for l_index, left in enumerate(nums[:-3]):
            r_index = len(nums) - 1
            m_index = l_index + 1

            while m_index < r_index:
                right = nums[r_index]
                middle = nums[m_index]
                print(left, middle, right)
                sum = left + middle + right
                test_diff = abs(sum - target)
                if least_diff is None or test_diff < least_diff:
                    least_diff = test_diff

                if sum > target:
                    # if sum is too big, move right to be decrease
                    r_index -= 1
                elif sum < target:
                    # if sum too small, move middle index to increase
                    m_index += 1
                elif sum == target:
                    return target

        return least_diff




sol = Solution()
sol.threeSumClosest([-1,2,1,-4], 1)