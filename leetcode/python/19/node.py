# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def findLengthList(self, head):
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        return count

    def removeNode(self, head, node_remove):
        count = 0
        node = head
        answer = []
        while node:
            if count != node_remove:
                answer.append(node.val)
            node = node.next
            count += 1

        return answer

    def makeNodeList(self, values):
        h = None
        for val in reversed(values):
            h = ListNode(val, h)
        return h

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = findLengthList(head)
        node_remove = n - l - 1
        values = removeNode(head, node_remove)
        node_answer = makeNodeList(values)
        return node_answer


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
