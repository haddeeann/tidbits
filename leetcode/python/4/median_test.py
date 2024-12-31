from m_2 import Solution

tests = [
    {
        'arr1': [1, 2],
        'arr2': [3, 4],
        'answer': 2.5
    }
]

sol = Solution()
answer = sol.findMedianSortedArrays(tests[0]['arr1'], tests[0]['arr2'] )
print(answer)