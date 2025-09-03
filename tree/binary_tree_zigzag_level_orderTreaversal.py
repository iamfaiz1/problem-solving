# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        count = 0
        queue = [root]
        while queue:
            size = len(queue) #this is for trversing level wise
            li = []   #thiss is to store level wise answer
            
            for i in range(size):
                node = queue.pop(0)
                li.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if count%2 ==0:
                ans.append(li)
            else:
                ans.append(li[::-1])
            count +=1
        return ans