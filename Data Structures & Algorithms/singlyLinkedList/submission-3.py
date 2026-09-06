class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if self.head == None:
            return -1

        current = self.head
        while index > 0:
            if current.next:
                current = current.next
                index -= 1
            elif current.next == None and index >=0:
                return -1
        return current.data
        
    def insertHead(self, val: int) -> None:
        node = LinkedListNode(val)
        node.next = self.head
        self.head = node

    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.insertHead(val)
        else:
            node = LinkedListNode(val)
            current = self.head
            while current.next:
                current = current.next
            current.next = node


    def remove(self, index: int) -> bool:

        if self.head == None:
            return False

        current = self.head
        prev = self.head

        if index == 0:
            self.head = current.next
        
        while index > 0:
            if current.next:
                prev = current
                current = current.next
                index -= 1
            elif current.next == None and index >=0:
                return False
    
        prev.next = current.next
        return True

    def getValues(self) -> List[int]:
        current = self.head
        ans = []
        while current:
            ans.append(current.data)
            current = current.next
        return ans
