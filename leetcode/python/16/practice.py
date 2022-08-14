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