class Solution(object):
    def nextPermutation(self):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums = ["a", "b", "c", "d", "pop"]
        i = len(nums) - 1
        swap = nums[i]
        nums.remove(swap)
        while i >= 0:
            nums.insert(i, swap)
            print(i, nums)
            nums.remove(swap)
            i -= 1



arr = [1, 2, 3]

answer = [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]

sol = Solution()
sol.nextPermutation()


answer_2 = [
    [1, 2, 3, 4, 5],

    [1, 2, 3, 5, 4],

    [1, 2, 5, 3, 4],
    [1, 2, 5, 4, 3],

    [1, 5, 2, 3, 4],
    [1, 5, 4, 2, 3],
    [1, 5, 4, 3, 2],

    [2, 1, 3, 4, 5],
    [2, 5, 1, 3, 4],
    [2, 5, 4, 1, 3],
    [2, 5, 4, 3, 1],

    [2, 5, 3, 1, 4],
    [2, 5, 3, 4, 1],

    [2, 5, 1, 3, 4],
]
