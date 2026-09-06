class ListNode:
    def __init__(self, value = 0):
        self.val = value
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        
        return curr.next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
    
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        
        # traverse to the index 
        curr = self.head
        for i in range(index):
            curr = curr.next
        
        next_node = curr.next

        new_node = ListNode(val)
        
        new_node.next = next_node
        new_node.prev = curr
        curr.next = new_node
        next_node.prev = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        # Find the node being deleted.
        node = self.head.next

        for _ in range(index):
            node = node.next

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)