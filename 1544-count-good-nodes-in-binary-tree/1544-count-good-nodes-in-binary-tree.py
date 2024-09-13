# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = []
        stack = [[root, root.val]]
        count = 0
        
        while stack:
            node, prevMax = stack.pop()
            if node:
                if node.val >= prevMax:
                    prevMax = node.val
                    count += 1
                
                stack.append([node.left, prevMax])
                stack.append([node.right, prevMax])

        return count
            
                
            



        
        