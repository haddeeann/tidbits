class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer_list = []
        nums.sort()
        print(nums)
        for index, test_num in enumerate(nums[:-2]):
            if index != 0 and test_num == nums[index-1]:
                continue
            left_index = index + 1
            right_index = len(nums) - 1
            while left_index < right_index:
                left = nums[left_index]
                right = nums[right_index]
                sum = test_num + left + right
                if sum > 0:
                    right_index -= 1
                elif sum < 0:
                    left_index += 1
                elif sum == 0:
                    answer_list.append([test_num, nums[left_index], nums[right_index]])
                    while left == nums[left_index] and left_index < right_index:
                        left_index += 1

        return answer_list


sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))