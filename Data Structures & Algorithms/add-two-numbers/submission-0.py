# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_root = ListNode(0)
        
        prev_carry = 0

        curr1 = l1
        curr2 = l2
        res_cur = res_root

        i = 0

        while (curr1) or (curr2) or prev_carry != 0:
            sum = 0
            if curr1:
                sum += curr1.val
            if curr2:
                sum += curr2.val
            
            sum += prev_carry
            rem = sum % 10
            carry = sum // 10

            prev_carry = carry

            res_cur.next = ListNode(rem)
            res_cur = res_cur.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next

        return res_root.next