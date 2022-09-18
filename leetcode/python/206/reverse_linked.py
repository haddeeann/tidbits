# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r = []
        while head:
            print(head.val)
            r.insert(0, head.val)
            head = head.next

        return createLinkedList(r)


# https://stackoverflow.com/questions/71569455/traverse-listnode-in-python
def createLinkedList(values):
    h = None
    for val in reversed(values):
        h = ListNode(val, h)

    return h


input = createLinkedList([1,2,3,4,5])
s = Solution()
s.reverseList(input)
a = [5,4,3,2,1]