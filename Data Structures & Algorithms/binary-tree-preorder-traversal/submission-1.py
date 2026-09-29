# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # def preorderHelper(self, root, arr):
    #     if root is None:
    #         return None
        
    #     arr.append(root.val)
    #     self.preorderHelper(root.left, arr)
    #     self.preorderHelper(root.right, arr)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []

        stack.append(root)
        
        while len(stack) > 0:
            out = stack.pop()

            if out and out.right is not None:
                stack.append(out.right)
            
            if out and out.left is not None:
                stack.append(out.left)
                
            if out:
                ans.append(out.val)
        
        return ans