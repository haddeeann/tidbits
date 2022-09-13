# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        while list1.next and list2.next:
            print(list1.val)


# https://stackoverflow.com/questions/71569455/traverse-listnode-in-python
def createLinkedList(values):
    head = None
    for val in reversed(values):
        head = ListNode(val, head)

    return head


sol = Solution()
list_node_1 = ListNode()
l_1 = createLinkedList([1, 2, 4])
print(l_1)

test_cases = [
    {
        "no": "one",
        "input_1": ListNode([1, 2, 4]),
        "input_2": ListNode([1, 3, 4]),
        "answer": ListNode([1, 1, 2, 3, 4, 4])
    },
    {
        "no": "two",
        "input_1": ListNode([]),
        "input_2": ListNode([]),
        "answer": ListNode([])
    },
    {
        "no": "three",
        "input_1": ListNode([]),
        "input_2": ListNode([0]),
        "answer": ListNode([0])
    }
]

for test in test_cases:
    result = sol.mergeTwoLists(test["input_1"], test["input_2"])
    if result == test["answer"]:
        print("answer is RIGHT")
    else:
        print("failed")