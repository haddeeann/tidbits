class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedList(values):
    h = None
    for val in reversed(values):
        h = ListNode(val, h)

    return h

def evenOdd(linked):
    first = ListNode()
    last = ListNode()
    while linked:
        print(linked.val)
        linked = linked.next

tests = [
    {
        "input": [5, 1, 3, 7, 3]
    }
]

for test in tests:
    linked_list = createLinkedList(test["input"])
    evenOdd(linked_list)