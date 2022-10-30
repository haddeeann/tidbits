# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            start = 0
            stop = amount - interval
            step = interval * 2
            for i in range(start, stop, step):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def mergeTwoLists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            pont.next=l1
        return head.next


def createLinkedList(values):
    h = None
    for val in reversed(values):
        h = ListNode(val, h)

    return h


sol = Solution()
l = []
og_list = [[1,4,5],[1,3,4],[2,6]]
for item in og_list:
    l.append(createLinkedList(item))
sol.mergeKLists(l)