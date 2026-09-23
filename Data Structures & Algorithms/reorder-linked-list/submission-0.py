# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Brute force/ Naive approach

        traveler = head
        # 1. have start = 0 , and travel to end
        # 2. tmp = start.next, start.next = end, end.next = tmp
        # 3. start = end.next

        while traveler:
            
            start = traveler
            end = traveler
            prev = traveler

            while end.next:
                prev = end
                end = end.next
            if start != prev:
                tmp = start.next
                start.next = end
                end.next = tmp
                prev.next = None
            else:
                end.next = None

            traveler = end.next