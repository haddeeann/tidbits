from longest_2 import Solution
sol = Solution()
t = [

]
tests = [
    {
        'input': 'abcabcbb',
        'answer': 3
    },
    {
        'input': 'abcabcbb',
        'answer': 3
    },
    {
        'input': 'aabcdee',
        'answer': 5
    },
    {
        'input': 'au',
        'answer': 2
    },
    {
        'input': 'dvdf',
        'answer': 3
    }
]
for test in tests:
    print('input: ', test['input'])
    a = sol.lengthOfLongestSubstring(test['input'])
    print(test['input'], a == test['answer'])
    print('------')