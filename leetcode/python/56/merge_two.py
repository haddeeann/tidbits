class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result_list = []
        last_result = None
        add_single = True

        def sort_intervals(e):
            return e[0]

        intervals.sort(key=sort_intervals)

        def test_overlap(left, test_arr):
            return left[0] <= test_arr[0] <= left[1] or left[0] <= test_arr[1] <= left[1]

        def make_overlap(left, right):
            # add the correct overlap
            small_left = min(left[0], right[0])
            large_right = max(left[1], right[1])
            result_list.append([small_left, large_right])

        def change_overlap(index, left, right):
            # fix the correct overlap
            small_left = min(left[0], right[0])
            large_right = max(left[1], right[1])
            result_list[index] = [small_left, large_right]

        for i, right_arr in enumerate(intervals[1:], start=1):
            if add_single:
                left_arr = intervals[i - 1]
                if test_overlap(left_arr, right_arr):
                    make_overlap(left_arr, right_arr)
                    add_single = False
                else:
                    if i == 1:
                        result_list.append(right_arr)
                    add_single = True
            elif len(result_list) > 0:
                last_result = len(result_list) - 1
                if test_overlap(result_list[last_result], right_arr):
                    change_overlap(last_result, result_list[last_result], right_arr)
                    add_single = False
                else:
                    add_single = True
            if add_single:
                result_list.append(right_arr)

        return result_list


sol = Solution()
test_set = [
    {
        "no": "eighth",
        "interval": [[1,3]],
        "answer": [[1,3]]
    }
]
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
    },
    {
        "no": "sixth",
        "reset_values": [[1, 3], [2, 6], [8, 10], [15, 18]],
        "interval": [[1, 3], [2, 6], [8, 10], [15, 18]],
        "answer": [[1, 6], [8, 10], [15, 18]]
    },
    {
        "no": "seventh",
        "interval": [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]],
        "answer": [[1, 10]]
    }
]

for test in test_set:
    result = sol.merge(test['interval'])
    if result == test['answer']:
        print(f"{test['no']} answer is right")
    else:
        print(f"{test['no']} answer is wrong, the input is {test['interval']} the result is {result}")