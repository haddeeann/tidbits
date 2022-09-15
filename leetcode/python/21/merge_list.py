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
        arr = []
        while node_a or node_b:
            if node_a:
                arr.append(node_a.val)
                node_a = node_a.next
            if node_b:
                arr.append(node_b.val)
                node_b = node_b.next
        return createLinkedList(arr)




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
        "answer": createLinkedList([1, 1, 2, 3, 4, 4]),
        "l": len([1, 1, 2, 3, 4, 4])
    }
]

for test in test_cases:
    r = sol.mergeTwoLists(test["input_1"], test["input_2"])
    counter = 0
    a = test["answer"]
    while r or a:
        if r and a:
            if r.val == a.val:
                r = r.next
                a = a.next
                print("all good")
            else:
                print("Failed, not equal")
        else:
            print("failed, not equal")

    print("lack of failure is success")


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