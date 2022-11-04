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
            # original places
            first = head.next
            print(first.val)
            second = first.next
            print(second.val)
            third = second.next
            if third:
                print(third.val)
            # swap the second and make it first
            head.next = second
            # make the first the second
            second.next = first
            # put the next node on the original first node
            first.next = third
            # use the head as a looping point by putting the first on it
            head = first
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