class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = [nums[0]]
        for x in nums[1:]:
            last_answer = r[len(r)-1]
            next = last_answer + x
            r.append(next)
        return r


sol = Solution()

test_set = [
    {
        "no": "one",
        "input": [1,2,3,4],
        "output": [1,3,6,10]
    }
]

for t in test_set:
    answer = sol.runningSum(t["input"])
    if answer == t["output"]:
        print(f"test {t['no']} is passed")
    else:
        print(f"test {t['no']} has failed")