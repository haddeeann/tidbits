import math


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        iter_1 = 0
        end_1 = len(nums1)

        iter_2 = 0
        end_2 = len(nums2)

        first_median = None
        second_median = None

        median_num_1 = None
        median_num_2 = None

        counter = 0
        total_length = end_1 + end_2
        if total_length % 2 == 0:
            even = True
            median_num_1 = total_length / 2 - 1
            median_num_2 = total_length / 2
        else:
            even = False
            median_num_1 = math.floor(total_length/2)

        while iter_1 < end_1 or iter_2 < end_2:
            if even:
                if counter == median_num_1:
                    if iter_1 < end_1 and nums1[iter_1] < nums2[iter_2]:
                        first_median = nums1[iter_1]
                    elif iter_2 < end_2:
                        first_median = nums2[iter_2]
                elif counter == median_num_2:
                    if iter_1 < end_1 and nums1[iter_1] < nums2[iter_2]:
                        second_median = nums1[iter_1]
                    elif iter_2 < end_2:
                        second_median = nums2[iter_2]
                    break
            elif even is False and counter == median_num_1:
                if iter_1 < end_1 and nums1[iter_1] < nums2[iter_2]:
                    first_median = nums1[iter_1]
                elif iter_2 < end_2:
                    first_median = nums2[iter_2]
                break

            if iter_1 < end_1:
                if iter_2 == end_2 or nums1[iter_1] < nums2[iter_2]:
                    iter_1 += 1

            if iter_2 < end_2:
                if iter_1 == end_1 or nums2[iter_2] < nums1[iter_1]:
                    iter_2 += 1

            counter += 1

        if even:
            return (first_median + second_median) / 2
        else:
            return first_median


sol = Solution()
print(sol.findMedianSortedArrays([11, 12], [2, 3]))
