# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        tail = head
        for i in range(k):
            if not tail:
                return head
            tail = tail.next

        tail = self.reverseKGroup(tail, k)

        for i in range(k):
            print(i)
            next = head.next
            head.next = tail
            tail = head
            head = next

        return tail


def makeListNode(values):
    h = None
    for val in reversed(values):
        h = ListNode(val, h)
    return h


sol = Solution()
l_node = makeListNode([1,2,3,4,5,6])
sol.reverseKGroup(l_node, 3)