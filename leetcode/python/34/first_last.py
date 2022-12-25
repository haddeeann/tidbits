class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        a, b = None, None
        while left <= right:
            if nums[left] == target:
                a = target
            if nums[right] == target:
                b = target
            if a is None:
                left += 1
            if b is None:
                right -= 1

            if a is not None and b is not None:
                return [left, right]

        return [-1, -1]


tests = [
    # {
    #     "input": [5,7,7,8,8,10],
    #     "target": 8,
    #     "answer": [3, 4]
    # },
    {
        "input": [0,0,0,1,2,3],
        "target": 0,
        "answer": [0, 2]
    },
    # {
    #     "input": [1],
    #     "target": 1,
    #     "answer": [0, 0]
    # }
]
sol = Solution()
for t in tests:
    pass_test = True
    answer = sol.searchRange(t["input"], t["target"])
    for i, x in enumerate(answer):
        if t["answer"][i] != x:
            pass_test = False
            break
    if pass_test:
        print("pass tests")
    else:
        print("FAILED")