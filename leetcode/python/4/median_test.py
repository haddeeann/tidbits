from m_3 import Solution

tests = [
    {
        'arr1': [1, 2, 3, 4, 5],
        'arr2': [5, 6, 7, 8, 9, 10, 11, 12, 13],
        'answer': 2.5
    }
]

sol = Solution()
answer = sol.findMedianSortedArrays(tests[0]['arr1'], tests[0]['arr2'] )
print(answer)