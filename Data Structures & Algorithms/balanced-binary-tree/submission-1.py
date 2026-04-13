# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, node:TreeNode):
        if not node:
            return 0

        lh = self.getHeight(node.left)
        rh = self.getHeight(node.right)

        return max(lh,rh) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)

        if abs(lh - rh) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)