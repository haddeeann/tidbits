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
        ulist = []
        step = head
        while step:
            if step.val in ulist:
                return step
            ulist.append(step.val)
            step = step.next
        return -1

# https://stackoverflow.com/questions/71569455/traverse-listnode-in-python
def createLinkedList(values):
    h = None
    for val in reversed(values):
        h = ListNode(val, h)

    return h


l = createLinkedList([3, 2, 0, -4, 2, 5])
s = Solution()
s.detectCycle(l)
