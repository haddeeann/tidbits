# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pass


sol = Solution()

test_cases = [
    {
        "no": "one",
        "input_1": [1, 2, 4],
        "input_2": [1, 3, 4],
        "answer": [1, 1, 2, 3, 4, 4]
    },
    {
        "no": "two",
        "input_1": [],
        "input_2": [],
        "answer": []
    },
    {
        "no": "three",
        "input_1": [],
        "input_2": [0],
        "answer": [0]
    }
]

for test in test_cases:
    result = sol.mergeTwoLists(test["input"])
    if result == test["answer"]:
        print("answer is RIGHT")
    else:
        print("failed")