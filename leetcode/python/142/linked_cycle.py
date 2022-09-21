# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = {}
        while head and head.next:
            if head in h:
                return h
            h[head] = 0
            head = head.next


# https://stackoverflow.com/questions/71569455/traverse-listnode-in-python
def createLinkedList(values):
    h = None
    for val in reversed(values):
        h = ListNode(val, h)

    return h


l = createLinkedList([3, 2, 0, -4, 2, 5])
s = Solution()
s.detectCycle(l)
