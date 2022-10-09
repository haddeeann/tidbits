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
        print(head, n)


test_case = {
    "no": "one",
    "input": ([1,2,3,4,5], 2),
    "answer": [1,2,3,5],
}