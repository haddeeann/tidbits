class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            s = k - len(nums)
        else:
            s = k

        if len(nums) > 1 and s != 0:
            right = nums[-s:]
            left = nums[:-s]
            if len(right) > 0 and len(left) > 0:
                nums[:s] = right
                nums[s:] = left
            elif len(nums) != s:
                nums.reverse()

        print(nums)


# arr = [1, 2, 3]
# shift = 2
# answer [2, 3, 1]

# arr = [1]
# shift = 0
# answer [1]

# arr = [1, 2]
# shift = 0
# answer [1, 2]

# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# shift = 3

# arr = [1, 2]
# shift = 3
# answer [2, 1]

arr = [1, 2, 3]
shift = 4
# [3, 1, 2]

# arr = [1, 2]
# shift = 2
# answer [1, 2]
sol = Solution()
sol.rotate(arr, shift)
