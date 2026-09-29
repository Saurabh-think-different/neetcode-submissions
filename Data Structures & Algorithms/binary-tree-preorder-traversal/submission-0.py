# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorderHelper(self, root, arr):
        if root is None:
            return None
        
        arr.append(root.val)
        self.preorderHelper(root.left, arr)
        self.preorderHelper(root.right, arr)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.preorderHelper(root, arr)
        return arr