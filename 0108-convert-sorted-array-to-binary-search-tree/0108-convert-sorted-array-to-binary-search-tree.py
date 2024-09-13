# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def binary(arr):
            if not arr:
                return None
            # if len(arr) > 0:
                # anyone if condition can be written - 
                # second if - indent below code inside this
            mid = len(arr) // 2

            midNode = TreeNode(arr[mid])
            midNode.left = binary(arr[:mid])
            midNode.right = binary(arr[mid+1:])
        
            return midNode

        return binary(nums)

                       
        
            