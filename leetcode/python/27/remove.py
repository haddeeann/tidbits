class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        print(nums)
        return k


sol = Solution()
sol.removeElement([3,2,2,3], 3)