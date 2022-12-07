class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedList(values):
    h = None
    for val in reversed(values):
        h = ListNode(val, h)

    return h


def evenOdd(head):
    if head == None or head.next == None:
        return head

    odd_dummy = ListNode(-1)
    even_dummy = ListNode(-1)

    odd_tail = odd_dummy
    even_tail = even_dummy

    index = 0
    curr = head
    while curr != None:
        if index % 2 == 0:
            even_tail.next = curr
            even_tail = curr
        else:
            odd_tail.next = curr
            odd_tail = curr

        curr = curr.next
        index += 1

    even_tail.next = odd_dummy.next
    odd_tail.next = None

    return even_dummy.next


tests = [
    {
        "input": [5, 1, 3, 7, 3]
    }
]

for test in tests:
    linked_list = createLinkedList(test["input"])
    answer = evenOdd(linked_list)
    while answer:
        print(answer.val)
        answer = answer.next