# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.count = k
        def inOrder(node):
            if not node:
                return 0
            inOrder(node.left)
            self.count -= 1
            if self.count == 0:
                self.res= node.val
                return
            inOrder(node.right)

        inOrder(root)
        return self.res
        
        