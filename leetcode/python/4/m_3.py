class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            leftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            rightX = float('inf') if partitionX == x else nums1[partitionX]
            leftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            rightY = float('inf') if partitionY == y else nums2[partitionY]
            if leftX <= rightY and leftY <= rightX:
                # return answer
                if (x + y) % 2 == 1:
                    return max(maxX, maxY)
                else:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
            elif leftX > rightY:
                high = partitionX - 1
            else:
                low = partitionX + 1