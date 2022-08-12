class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        print(nums)
        print(len(nums))
        print(target)
        least_diff = None
        test_diff = 0
        sum = 0
        least_sum = 0

        if len(nums) <= 3:
            for num in nums:
                sum += num
            return sum

        # comment goes here
        for l_index, left in enumerate(nums[:-2]):
            r_index = len(nums) - 1
            m_index = l_index + 1

            while m_index < r_index:
                right = nums[r_index]
                middle = nums[m_index]

                sum = left + middle + right
                test_diff = abs(sum - target)
                print(left, middle, right)
                if least_diff is None or test_diff < least_diff:
                    least_diff = test_diff
                    least_sum = sum

                if sum > target:
                    # if there's repeats
                    prev_right = r_index - 1
                    if right == nums[prev_right]:
                        while right == nums[prev_right] and prev_right > l_index:
                            prev_right -= 1
                        r_index = prev_right
                    else:
                        # if sum is too big, move right to be decrease
                        r_index -= 1
                elif sum < target:
                    # if there's repeats
                    next_left = l_index + 1
                    if left == nums[next_left]:
                        while left == nums[next_left] and next_left < r_index:
                            next_left += 1
                        l_index = next_left
                    else:
                        # if sum too small, move middle index to increase
                        m_index += 1
                elif sum == target:
                    return target
        print(least_sum)
        return least_sum




sol = Solution()

# sol.threeSumClosest([0,0,0], 1)
# sol.threeSumClosest([1,1,1,1], 4)
sol.threeSumClosest([-4, -4, -1, 1, 2], 1)

# sol.threeSumClosest([524,428,969,-868,223,333,986,-553,-519,967,-392,709,82,-819,-188,-416,-359,477,-622,-912,-883,3,-278,-265,-195,791,-515,183,-239,-817,764,576,804,647,-743,-766,-642,461,-313,-90,4,882,-933,-921,-24,74,892,578,234,621,-825,806,192,227,-495,585,236,259,-384,873,456,182,93,33,-298,579,240,-922,980,-68,110,855,786,-814,924,-305,-217,-198,-64,634,686,-295,943,-140,-852,-460,190,-907,-311,584,545,-920,-366,902,-446,64,-676,702,-928,-17,-666,766,-493,-249,922,-910,673,-847,-338,-139,-831,-40,-873,271,-913,-448,57,-853,653,-560,-484,668,118,-601,-882,-414,-432,497,349,-605,-881,-324,-488,-443,663,558,684,996,-675,114,441,-144,815,281,286,505,-502,-457,216,678,-353,249,488,-347,-972,-555,-963,-860,87,112,-981,119,-141,834,587,511,-420,816,-838,194,-340,-996,-951,-717,45,-88,-636,-152,-662,-565,-872,-38,507,-76,606,490,-69,-247,-431,1,-777,-201,-52,-56,666,682,-160,174,941,478,178,-916,-832,911,-264,760,-463,-60,-516,-154,763,-762,-808,-850,129,-150,-641,564,649,52,-6,-309,83,655,780,769,388,-287,435,218,727,737,844,777,-528,-72,-781,439,885,-98,-44,-952,-325,-350,-966,650,-930,-388,494,630,313,-480,616,472,399,172,-290,24,669,-215,-504,761,486,-525,75,-131,-656,-979,916,-604,204,-684,-344,904,-619,370,-173,-2,-828,504,-505,-965,-811,221,-49,944,-499,-181,-301,250,753,384,-233,168,344,326,-580,202,39,-857,159,-97,-430,-452,433,256,-582,-165,235,73,-358,-608,871,957,954,-169,907,595,-986,-783,406,-481,-253,792,11], 7651)