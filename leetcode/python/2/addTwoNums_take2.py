# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, n=None):
        self.val = val
        self.next = n

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry
            carry = total // 10
            base = total % 10
            current.next = ListNode(base)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

def make_linked_list(new_list):
    head = ListNode(new_list[0])
    current = head

    for value in new_list[1:]:
        current.next = ListNode(value) # create a new node and link to it
        current = current.next # move to the next node

    return head

def print_linked_list(node):
    current = node
    while current:
        print(current.val)
        current = current.next

arr_1 = [9,9,9,9,9,9,9]
arr_2 = [9,9,9,9]
ll_1 = make_linked_list(arr_1)
ll_2 = make_linked_list(arr_2)
solution = Solution()
answer = solution.addTwoNumbers(ll_1, ll_2)
print_linked_list(answer)


