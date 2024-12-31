class Solution(object):
    def merge(self, left, right):
        sorted_array = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
        return sorted_array

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        # split the array into two halves
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        combined = nums1 + nums2
        answer = self.merge_sort(combined)
        if len(answer) % 2 == 0:
            mid = int(len(answer) / 2)
            prev_mid = mid - 1
            return (answer[mid] + answer[prev_mid]) / 2
        else:
            mid = round(len(answer) / 2)
            return answer[mid]