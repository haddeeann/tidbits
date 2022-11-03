def hereIam:
    if not head:
        return head
    dummy = ListNode(0)
    dummy.next, head = head, dummy
    while head.next and head.next.next:
        a, b = head.next, head.next.next
        head.next, a.next, b.next, head = b, b.next, a, a
    return dummy.next