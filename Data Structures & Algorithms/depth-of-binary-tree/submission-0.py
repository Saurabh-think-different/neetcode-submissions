# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMax(self, node, best):
        if node is None:
            return 0
        best += 1
        m1 = self.findMax(node.left, best)
        m2 = self.findMax(node.right, best)

        return max(m1, m2, best)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        best = 0
        return self.findMax(root, best)