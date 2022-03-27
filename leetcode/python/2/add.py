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
        addList = []
        if len(l1) >= len(l2):
            long = l1
            short = l2
        else:
            long = l2
            short = l1
        diff = len(long) - len(short)
        carry = None
        for x_idx, x in enumerate(long):
            if x_idx <= diff:
                addNum = short[x_idx] + long[x_idx] + carry if carry is not None else short[x_idx] + long[x_idx]
            else:
                addNum = long[x_idx] + carry if carry is not None else long[x_idx]

            if addNum > 9 and x_idx != len(long) - 1:
                strNum = str(addNum)
                addList.append(int(strNum[1]))
                carry = int(strNum[0])
            elif addNum > 9 and x_idx == len(long) - 1:
                strNum = str(addNum)
                addList.append(int(strNum[1]))
                addList.append(int(strNum[0]))
            else:
                addList.append(addNum)
                carry = 0
        return addList


sol = Solution()
print(sol.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
