# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return_list = ListNode()
        loop = return_list

        l1_list = l1
        l2_list = l2
        carry = 0

        while l1_list and l2_list:
            addSum = l1_list.val + l2_list.val + carry

            if addSum > 9:
                strSum = str(addSum)
                loop.val = int(strSum[1])
                carry = int(strSum[0])
            else:
                loop.val = addSum
                carry = 0

            if (l1_list is not None and l1_list.next is not None) or (l2_list is not None and l2_list.next is not None):
                loop.next = ListNode()

            # loop replacements
            l1_list = l1_list.next if l1_list is not None else None
            l2_list = l2_list.next if l2_list is not None else None

            if l1_list is None and l2_list is None and carry != 0:
                new_node = ListNode()
                new_node.val = 1
                loop.next = new_node
            else:
                loop = loop.next

        return return_list
