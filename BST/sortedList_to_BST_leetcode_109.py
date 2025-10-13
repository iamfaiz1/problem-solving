# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def BST(head):
            if not head:
                return None
            elif not head.next:
                return TreeNode(head.val)

            slow = head
            fast = head
            prev = None

            while(fast and fast.next):
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            root = TreeNode(slow.val)
            if(prev):
                prev.next = None

            root.left = BST(head)
            root.right = BST(slow.next)

            return root
        
        return BST(head)
            