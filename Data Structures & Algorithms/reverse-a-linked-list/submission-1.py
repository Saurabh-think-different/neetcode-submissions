# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prevEle = None
        currEle = head

        if not head:
            return head
        
        while currEle:
            next_node = currEle.next
            currEle.next = prevEle
            prevEle = currEle
            currEle = next_node
        return prevEle
        
