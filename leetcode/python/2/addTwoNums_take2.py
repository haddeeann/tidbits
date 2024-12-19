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
        l1_curr = l1
        l2_curr = l2
        l3 = ListNode()
        loop = l3
        carry = 0
        while l1_curr and l2_curr:
            add = l1_curr.val + l2_curr.val + carry
            if add > 9:
                carry = 1
                add_sum = add % 10
            else:
                carry = 0
                add_sum = add

            loop.val = add_sum
            if l1_curr.next or l2_curr.next:
                loop.next = ListNode()
                loop = loop.next
            l1_curr = l1_curr.next
            l2_curr = l2_curr.next
        while l1_curr:
            add = l1_curr.val + carry
            if add > 9:
                carry = 1
                add_sum = add % 10
            else:
                carry = 0
                add_sum = add
            loop.val = add_sum
            if l1_curr.next:
                loop.next = ListNode()
                loop = loop.next
            l1_curr = l1_curr.next
        while l2_curr:
            add = l2_curr.val + carry
            if add > 9:
                carry = 1
                add_sum = add % 10
            else:
                carry = 0
                add_sum = add
            loop.val = add_sum
            if l2_curr.next:
                loop.next = ListNode()
                loop = loop.next
            l2_curr = l2_curr.next
        if carry == 1:
            loop.next = ListNode()
            loop.val = 1
        return l3





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

arr_1 = [9,2,3,4,1]
arr_2 = [1,3,4,5]
ll_1 = make_linked_list(arr_1)
ll_2 = make_linked_list(arr_2)
solution = Solution()
answer = solution.addTwoNumbers(ll_1, ll_2)
print_linked_list(answer)


