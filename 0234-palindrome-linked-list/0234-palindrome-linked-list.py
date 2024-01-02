# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle of the list
        slow, fast = head, head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # slow points to the middle of the list
        #reverse the second part of the list from the middle
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        # check for palindrome 
        left, right = head, prev 
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True
            