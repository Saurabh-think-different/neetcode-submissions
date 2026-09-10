# Binary Search Tree Node
class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


# Implementation for Binary Search Tree Map
class TreeMap:
    def __init__(self):
        self.root = None
        self.min = -1
        self.max = -1

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if self.root == None:
            self.root = newNode
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                    break
                current = current.left
            elif key > current.key:
                if current.right == None:
                    current.right = newNode
                    break
                current = current.right
            else:
                current.val = val
                break
        
        min = self.findMin(self.root)
        self.min = min.val if min else -1

        max = self.findMax(self.root)
        self.max = max.val if max else -1

    def get(self, key: int) -> int:
        current = self.root
        while current != None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return -1

    def getMin(self) -> int:
        return self.min

    # Returns the node with the minimum key in the subtree
    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def findMax(self, node: TreeNode) -> TreeNode:
        while node and node.right:
            node = node.right
        return node

    def getMax(self) -> int:
        return self.max
    
    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

        min = self.findMin(self.root)
        self.min = min.val if min else -1

        max = self.findMax(self.root)
        self.max = max.val if max else -1

    # Returns the new root of the subtree after removing the key
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr == None:
            return None

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                # Replace curr with right child
                return curr.right
            elif curr.right == None:
                # Replace curr with left child
                return curr.left
            else:
                # Swap curr with inorder successor
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
            

# 1
#   \
#    \
#     \ 
#      4
#     / \
#    3.  5
#   /
#  2