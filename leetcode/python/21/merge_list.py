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
        node_a = list1
        node_b = list2
        while node_a or node_b:
            if node_a:
                print(node_a.val)
                node_a = node_a.next
            elif node_b:
                print(node_b.val)
                node_b = node_b.next



# https://stackoverflow.com/questions/71569455/traverse-listnode-in-python
def createLinkedList(values):
    head = None
    for val in reversed(values):
        head = ListNode(val, head)

    return head


sol = Solution()

test_cases = [
    {
        "no": "one",
        "input_1": createLinkedList([1, 2, 4]),
        "input_2": createLinkedList([1, 3, 4]),
        "answer": createLinkedList([1, 1, 2, 3, 4, 4])
    }
]

for test in test_cases:
    result = sol.mergeTwoLists(test["input_1"], test["input_2"])
    # if result == test["answer"]:
    #     print("answer is RIGHT")
    # else:
    #     print("failed")


backup = [
    {
        "no": "two",
        "input_1": createLinkedList([]),
        "input_2": createLinkedList([]),
        "answer": createLinkedList([])
    },
    {
        "no": "three",
        "input_1": createLinkedList([]),
        "input_2": createLinkedList([0]),
        "answer": createLinkedList([0])
    }
]