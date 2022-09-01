class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result_list = []
        overlap = None
        count = 0

        def sort_intervals(e):
            return e[0]

        intervals.sort(key=sort_intervals)

        def test_overlap(left_arr, test_arr):
            return left_arr[0] <= test_arr[0] <= left_arr[1] or left_arr[0] <= test_arr[1] <= left_arr[1]

        def make_overlap(left, right):
            # add the correct overlap
            small_left = min(left[0], right[0])
            large_right = max(left[1], right[1])
            result_list.append([small_left, large_right])

        def change_overlap(index, right):
            left = result_list[index]
            # fix the correct overlap
            small_left = min(left[0], right[0])
            large_right = max(left[1], right[1])
            result_list[index] = [small_left, large_right]

        for i, left_arr in enumerate(intervals):
            if overlap:
                overlap = False
                continue
            if i != len(intervals) - 1:
                # test overlap
                overlap = test_overlap(left_arr, intervals[i+1])
                if overlap:
                    make_overlap(left_arr, intervals[i+1])
                else:
                    result_list.append(left_arr)
            else:
                for i, arr in enumerate(result_list):
                    if test_overlap(arr, left_arr):
                        change_overlap(i, left_arr)
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
    },
    {
        "no": "fourth",
        "interval": [[1, 4], [0, 5]],
        "answer": [[0, 5]]
    },
    {
        "no": "fifth",
        "interval": [[1, 4], [0, 2], [3, 5]],
        "answer": [[0, 5]]
    }
]
test_set = [
    {
        "no": "sixth",
        "interval": [[1,3],[2,6],[8,10],[15,18]],
        "answer": [[1,6],[8,10],[15,18]]
    }
]

for test in test_set:
    result = sol.merge(test['interval'])
    if result == test['answer']:
        print(f"{test['no']} answer is right")
    else:
        print(f"{test['no']} answer is wrong")