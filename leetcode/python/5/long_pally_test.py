from long_pally2 import Solution

tests = [
    {
        'input': 'aacabdkacaa',
        'answer': 'aca'
    },
    {
        'input': 'abcbe',
        'answer': 'bcb'
    },
    {
        'input': 'abcba',
        'answer': 'abcba'
    },
    {
        'input': 'ccc',
        'answer': 'ccc'
    },
    {
        'input': 'a',
        'answer': 'a'
    },
    {
        'input': 'abcdefghi',
        'answer': 'a'
    },
    {
        'input': 'babad',
        'answer': 'bab'
    },
    {
        'input': 'cbbd',
        'answer': 'bb'
    }
]

sol = Solution()
for test in tests:
    answer = sol.longestPalindrome(test['input'])
    if answer == test['answer']:
        print('correct: ', test['input'])
    else:
        print('incorrect: ', test['input'])