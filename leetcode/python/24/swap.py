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
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head.next and head.next.next:
            a = head.next
            b = head.next.next
            head.next = b
            a.next = b.next
            b.next = a
            head = a
        return dummy.next

def createLinkedList(values):
    h = None
    for val in reversed(values):
        h = ListNode(val, h)

    return h


sol = Solution()
l = [1,2,3,4,5,6]

ll = createLinkedList(l)
sol.swapPairs(ll)