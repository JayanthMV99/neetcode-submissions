# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxD = 0
    
    def getHeight(self, node: TreeNode):
        if not node:
            return 0

        lftH = self.getHeight(node.left)
        rgtH = self.getHeight(node.right)

        self.maxD = max(self.maxD, lftH + rgtH)

        return 1 + max(lftH, rgtH)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getHeight(root)
        return self.maxD