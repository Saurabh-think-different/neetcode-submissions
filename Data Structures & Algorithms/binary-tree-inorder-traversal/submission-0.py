# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderHelper(self, root, arr):
        if root is None:
            return None

        self.inorderHelper(root.left, arr)
        arr.append(root.val)
        self.inorderHelper(root.right, arr)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.inorderHelper(root, arr)
        return arr