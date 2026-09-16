# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev = curr = head

        while curr and curr.next:
            prev = prev.next
            curr = curr.next.next
            if curr == prev:
                return True
        return False
        
        