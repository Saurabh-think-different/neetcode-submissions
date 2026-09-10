# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, node):
        while node.left:
            node = node.left
        return node
    
    def findNodetoDelete(self, node, key):
        prev = None
        curr = node

        while curr:
            if key < curr.val:
                prev = curr
                curr = curr.left

            elif key > curr.val:
                prev = curr
                curr = curr.right

            else:
                return prev, curr

        return None, None
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        prev_node, target_node = self.findNodetoDelete(root, key)
        
        if not target_node:
            return root

        if not target_node.left and not target_node.right:

            # target is root
            if prev_node is None:
                return None

            if prev_node.left == target_node:
                prev_node.left = None
            else:
                prev_node.right = None

        elif target_node.left and not target_node.right:
            if prev_node is None:
                return target_node.left

            if prev_node.left == target_node:
                prev_node.left = target_node.left
            else:
                prev_node.right = target_node.left
        
        elif not target_node.left and target_node.right:
            if prev_node is None:
                return target_node.right

            if prev_node.left == target_node:
                prev_node.left = target_node.right
            else:
                prev_node.right = target_node.right
        
        else:
            min_node = self.findMin(target_node.right)

            target_node.val = min_node.val

            # Now delete successor
            successor_parent = target_node
            successor = target_node.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        return root
