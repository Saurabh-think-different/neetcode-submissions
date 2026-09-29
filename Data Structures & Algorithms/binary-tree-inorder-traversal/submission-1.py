# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def inorderHelper(self, root, arr):
    #     if root is None:
    #         return None

    #     self.inorderHelper(root.left, arr)
    #     arr.append(root.val)
    #     self.inorderHelper(root.right, arr)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []

        curr = root
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        while len(stack) > 0:
            out = stack.pop()

            curr = out.right
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            ans.append(out.val)

        return ans
