# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # move slow to the head if both nodes are equal
            if slow == fast:
                slow = head
                # break thru the loop if slow.next and fast.next are equal -> cycle and return True
                while slow.next != fast.next:
                    slow = slow.next
                    fast = fast.next
                return True
        # return False -> no cycle
        return False
        