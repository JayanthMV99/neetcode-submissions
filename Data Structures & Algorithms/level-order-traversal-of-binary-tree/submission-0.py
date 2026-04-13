# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []

        def order(node, level):
            if len(self.ans) == level:
                self.ans.append([])

            self.ans[level].append(node.val)

            if node.left:
                order(node.left, level+1)
            if node.right:
                order(node.right, level+1)

        if not root:
            return self.ans

        order(root, 0)
        return self.ans