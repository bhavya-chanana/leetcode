# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()

        res = []
        if root:
            q.append(root)
            
        while q:
            for i in range(len(q)):
                rightnode = None
                node = q.popleft()
                rightSide = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(node.val)

        return res
        