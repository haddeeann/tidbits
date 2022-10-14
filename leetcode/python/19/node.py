# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        node = head
        new_linked = []
        while node:
            count += 1
            node = node.next

        print(count)
        node_remove = n - count
        count = 0
        while node:
            new_linked.append(node.val)
            count += 1
            node = node.next
            if count == node_remove:
                skip
        print(new_linked)


def createLinkedList(values):
    h = None
    for val in reversed(values):
        h = ListNode(val, h)
    return h


test_case = {
    "no": "one",
    "input": ([1, 2, 3, 4, 5], 2),
    "answer": [1, 2, 3, 5],
}

s = Solution()
c = [1, 2, 3, 4, 5]
node_list = createLinkedList(c)
s.removeNthFromEnd(node_list, 2)
