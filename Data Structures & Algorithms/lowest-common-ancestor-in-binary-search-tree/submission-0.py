# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parentVal = root.val
        pVal = p.val
        qVal = q.val

        if pVal < parentVal and qVal < parentVal:
            return self.lowestCommonAncestor(root.left, p, q)
        elif pVal > parentVal and qVal > parentVal:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root