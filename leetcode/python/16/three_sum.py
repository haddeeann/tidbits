class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        print('nums: ', nums)
        for l_index, left in enumerate(nums[:-2]):
            sums_arr = []
            m_index = l_index + 1
            middle = nums[m_index]

            r_index = len(nums) - 1
            right = nums[r_index]

            least_diff = None
            least_sum = None
            while m_index < r_index:
                sum = left + middle + right
                sums_arr.append(sum)
                diff = abs(sum-target)
                if least_diff is None or diff < least_diff:
                    least_diff = diff
                    least_sum = sum

                if sum > target:
                    # move right index
                    r_index -= 1
                    right = nums[r_index]
                elif sum < target:
                    # move middle index
                    m_index += 1
                    middle = nums[m_index]
            print(sums_arr)
        return least_sum


sol = Solution()
# set one, inputs
test_set = [
    {
        "n": 1,
        "answer": 2,
        "arr": [-1,2,1,-4],
        "t": 1
    }
]

for item in test_set:
    result = sol.threeSumClosest(item["arr"], item["t"])
    if item["answer"] == result:
        print(f"test {item['n']} has passed")
    else:
        print(f"test {item['n']} FAILED")
