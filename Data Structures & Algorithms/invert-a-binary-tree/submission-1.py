# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseNode(self, node):
        if node is None:
            return None
        node.left, node.right = node.right, node.left
        self.reverseNode(node.left)
        self.reverseNode(node.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reverseNode(root)
        return root

