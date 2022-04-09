import math


def find_median_value(i_1, i_2, nums1, nums2):
    if i_1 < len(nums1) and i_2 < len(nums2):
        if nums1[i_1] <= nums2[i_2]:
            return float(nums1[i_1])
        if nums2[i_2] < nums1[i_1]:
            return float(nums2[i_2])
    elif i_1 < len(nums1):
        return float(nums1[i_1])
    elif i_2 < len(nums2):
        return float(nums2[i_2])


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        counter = 0
        total_length = (len(nums1) + len(nums2))
        even = total_length % 2 == 0
        odd = total_length % 2 != 0

        # iterators
        i_1 = 0
        i_2 = 0

        # index median finders
        if even:
            first_median = int((total_length / 2) - 1)
            median = int(total_length / 2)
        elif odd:
            median = int(math.floor(total_length / 2))

        # median values
        first_median_value = None
        second_median_value = None
        median_value = None
        while counter <= median:
            if even:
                if counter == first_median:
                    first_median_value = find_median_value(i_1, i_2, nums1, nums2)
                if counter == median:
                    second_median_value = find_median_value(i_1, i_2, nums1, nums2)

                    if first_median_value is not None and second_median_value is not None:
                        median_value = (first_median_value + second_median_value) / 2
            if odd:
                if counter == median:
                    median_value = find_median_value(i_1, i_2, nums1, nums2)

            if i_1 < len(nums1) and i_2 < len(nums2):
                if nums1[i_1] <= nums2[i_2]:
                    i_1 += 1
                elif nums2[i_2] < nums1[i_1]:
                    i_2 += 1
            elif i_1 < len(nums1):
                i_1 += 1
            elif i_2 < len(nums2):
                i_2 += 1

            counter += 1

        print(median_value)
        return median_value


sol = Solution()
# median odd
# floor(length / 2)

# median even
# first_median = (length / 2) - 1
# second_median = length / 2

sol.findMedianSortedArrays([1, 2], [3, 4])
