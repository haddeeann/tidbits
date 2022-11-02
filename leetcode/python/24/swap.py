# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next, head = head, dummy
        while head.next and head.next.next:
            a, b = head.next, head.next.next
            head.next, a.next, b.next, head = b, b.next, a, a
        return dummy.next

def createLinkedList(values):
    h = None
    for val in reversed(values):
        h = ListNode(val, h)

    return h


sol = Solution()
l = [1,2,3,4]

ll = createLinkedList(l)
sol.swapPairs(ll)