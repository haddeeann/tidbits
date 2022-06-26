class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        upCount = 0
        downCount = len(numbers) - 1
        testAdd = None
        while upCount < downCount or target != testAdd:
            up = numbers[upCount]
            down = numbers[downCount]
            sum = up + down
            if sum == target:
                return [upCount + 1, downCount + 1]
            elif sum > target:
                downCount -= 1
            elif sum < target:
                upCount += 1


sol = Solution()
ans = sol.twoSum([2, 7, 11, 15], 9)
print(ans)