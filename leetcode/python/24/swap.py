# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swap(self, node1, node2):
        temp = node1
        node1 = node2
        node2 = node1

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        while temp and temp.next:
            temp = a
            a = b
            b = fuck
        return head


def createLinkedList(values):
    h = None
    for val in reversed(values):
        h = ListNode(val, h)

    return h


sol = Solution()
l = [1,2,3,4]

ll = createLinkedList(l)
sol.swapPairs(ll)