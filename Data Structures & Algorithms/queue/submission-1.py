class ListNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1, None, None)
        self.tail = ListNode(-1, self.head, None)

        self.head.next = self.tail
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0 

    def append(self, value: int) -> None:
        last_node = self.tail.prev

        new_node = ListNode(value, last_node, self.tail)

        self.tail.prev = new_node
        last_node.next = new_node
        self.size += 1

    def appendleft(self, value: int) -> None:
        
        first_node = self.head.next

        new_node = ListNode(value, self.head, first_node)
        self.head.next = new_node
        first_node.prev = new_node

        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        last_node = self.tail.prev # needs to be popped

        self.tail.prev = last_node.prev
        last_node.prev.next = self.tail
        
        last_node.next = last_node.prev = None
        self.size -= 1

        return last_node.value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next # needs to be popped

        first_node.next.prev = self.head
        self.head.next = first_node.next

        first_node.prev = first_node.next = None

        self.size -= 1
        
        return first_node.value
