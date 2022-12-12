class Solution(object):
    def nextPermutation(self):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums = [1, 2, 3, 4, 5]
        i = len(nums) - 1
        right = None
        reverse = True
        while i >= 1:
            if nums[i - 1] < nums[i]:
                left_i = i - 1
                left = nums[i - 1]
                j = i
                while j < len(nums):
                    if nums[j] > left:
                        if not right or nums[j] <= right:
                            right = nums[j]
                            right_i = j
                    j += 1
                nums[left_i] = right
                nums[right_i] = left
                nums[i:] = nums[i:][::-1]
                reverse = False
                break
            i -= 1
        if reverse:
            nums.reverse()


test = [2, 3, 1, 3, 3]

sol = Solution()
sol.nextPermutation(test)
