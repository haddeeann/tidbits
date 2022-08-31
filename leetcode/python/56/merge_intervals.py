class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result_list = []
        overlap = None

        def sort_intervals(e):
            return e[0]

        intervals.sort(key=sort_intervals)

        def test_small(small_arr, t_1, t_2):
            overlap_test = False
            first_small = small_arr[0]
            second_small = small_arr[1]
            if first_small <= t_1 <= second_small:
                overlap_test = True
            if first_small <= t_2 <= second_small:
                overlap_test = True

            return overlap_test

        for i, small in enumerate(intervals):
            if overlap:
                overlap = False
                continue
            if i == len(intervals) - 1:
                # if last one then just add, if we haven't skipped last due to overlap
                result_list.append(small)
            else:
                next_small = intervals[i+1]
                # test overlap
                overlap = test_small(small, next_small[0], next_small[1])
                if overlap:
                    # add the correct overlap
                    smallest_left = min(small[0], next_small[0])
                    largest_right = max(small[1], next_small[1])
                    result_list.append([smallest_left, largest_right])
                else:
                    result_list.append(small)
        print(result_list)
        return result_list


sol = Solution()
backup_tests = [
    {
        "no": "first",
        "interval": [[1, 3], [2, 6], [8, 10], [15, 18]],
        "answer": [[1, 6], [8, 10], [15, 18]]
    },
    {
        "no": "second",
        "interval": [[1, 4], [4, 5]],
        "answer": [[1, 5]]
    },
    {
        "no": "third",
        "interval": [[1, 4], [0, 4]],
        "answer": [[0, 4]]
    }
]
test_set = [
    {
        "no": "fourth",
        "interval": [[1,4],[0,5]],
        "answer": [[0,5]]
    }
]

for test in test_set:
    result = sol.merge(test['interval'])
    if result == test['answer']:
        print(f"{test['no']} answer is right")
    else:
        print(f"{test['no']} answer is wrong")