'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        # Code here
        def successor(root):
            while root.left:
                root = root.left
            return root.data
        
        def find(root):
            if not root:
                return None
            
            # this condition covers if x has right subtree (optimization).
            if x.right:
                return successor(x.right)
            # findding
            suc = None
            cur = root
            
                
            while cur is not None:
                if cur.data > x.data:
                    suc = cur
                    cur = cur.left
                elif cur.data <= x.data:
                    cur = cur.right
                else:
                    if cur.data==x.data and cur.right:
                        return successor(x.right)
            if suc:
                return suc.data
            else:
                return -1
        return find(root)