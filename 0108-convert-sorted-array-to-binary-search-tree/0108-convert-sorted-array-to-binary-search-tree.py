# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def binary(arr):
            if not arr:
                return None
            if len(arr) > 0:
                mid = len(arr) // 2
                left, right = mid - 1, mid + 1
                midNode = TreeNode(arr[mid])
            
                if left >= 0 and left < len(arr):
                    midNode.left = binary(arr[:mid])
                if right < len(arr):
                    midNode.right = binary(arr[mid+1:])
            
                return midNode

        return binary(nums)

                       
        
            