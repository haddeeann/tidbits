# Definition for singly-linked list.
import math
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r = []
        while head:
            r.append(head.val)
            head = head.next

        midpoint = round(len(r) / 2)
        print(midpoint)
        half = r[midpoint:]
        return createLinkedList(half)


# https://stackoverflow.com/questions/71569455/traverse-listnode-in-python
def createLinkedList(values):
    h = None
    for val in reversed(values):
        h = ListNode(val, h)

    return h


s = Solution()

input = createLinkedList([1, 2, 3, 4, 5])
a = [3, 4, 5]
s.middleNode(input)
