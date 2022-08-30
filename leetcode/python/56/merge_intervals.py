class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result_list = []
        overlap = None
        def test_small(small, t_1, t_2):
            overlap = False
            first_small = small[0]
            second_small = small[1]
            if first_small <= t_1 <= second_small:
                overlap = True
            if first_small <= t_2 <= second_small:
                overlap = True

            return overlap

        for i, small in enumerate(intervals):
            if overlap:
                overlap = False
                continue
            if i == len(intervals) - 1:
                result_list.append(small)
            else:
                next_small = intervals[i+1]
                overlap = test_small(small, next_small[0], next_small[1])
                if overlap:
                    result_list.append([small[0], next_small[1]])
                else:
                    result_list.append(small)
        print(result_list)
        return result_list


sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
result = sol.merge(intervals)
answer = [[1,6],[8,10],[15,18]]

if result == answer:
    print("first answer is right")
else:
    print("first answer is wrong")

intervals = [[1,4],[4,5]]
result = sol.merge(intervals)
answer = [[1,5]]

if result == answer:
    print("second answer is right")
else:
    print("second answer is wrong")

# [[1,4],[0,4]]
# [[0,4]]