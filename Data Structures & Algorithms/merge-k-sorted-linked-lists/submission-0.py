# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def merge2Lists(self, list1, list2) -> Optional[ListNode]:
        head = ListNode(-1)
        l = list1
        r = list2
        curr = head

        while l and r:
            if l.val <= r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next
        if r == None and l:
            curr.next = l
        else:
            curr.next = r

        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        s = 0
        e = k
        mid = int((s+e)/2)
        if k == 0:
            return None
        if k == 1:
            return lists[0]
        head1 = self.mergeKLists(lists[s:mid])
        head2 = self.mergeKLists(lists[mid:e])
        return self.merge2Lists(head1, head2)
        