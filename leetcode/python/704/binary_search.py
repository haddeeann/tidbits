import math
class Solution(object):
    def get_middle(self, arr):
        return int(math.floor(len(arr)/2))

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        iterator = self.get_middle(nums)
        new_list = nums
        index = 0

        if nums[iterator] == target:
            return iterator

        while len(new_list) > 1:
            middle_value = new_list[iterator]
            if target < middle_value:
                # get the left side of the list
                new_list = new_list[:iterator]
                iterator = self.get_middle(new_list)
                if len(new_list) == 1 and new_list[iterator] == target:
                    return iterator
            elif target > middle_value:
                # get left side of the list
                index += len(new_list[:iterator])
                # get the right side of list
                new_list = new_list[iterator:]
                iterator = self.get_middle(new_list)
            elif middle_value == target:
                answer = index + iterator
                return answer

        return -1


sol = Solution()
print(sol.search([2, 5], 2))