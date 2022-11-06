class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i, n in enumerate(nums):
            if i != len(nums) - 1:
                if n != nums[i+1]:
                    nums[count] = n
                    count += 1
            else:
                index = count - 1 if count > 0 else 0
                if n != nums[index] or count == 0:
                    nums[count] = n
                    count += 1

        print(count)
        return count


sol = Solution()
sol.removeDuplicates([1,1,1])