class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


def makeListNode(list_input):
    h = None
    for val in reversed(list_input):
        h = ListNode(val, h)
    return h


l = makeListNode([1, 2])
s = Solution()
s.hasCycle(l)
