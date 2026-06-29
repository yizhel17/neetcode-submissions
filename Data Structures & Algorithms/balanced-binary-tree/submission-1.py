# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0
            
            le = dfs(node.left)
            if le == -1:
                return -1
            
            ri = dfs(node.right)
            if ri == -1:
                return -1

            if abs(le - ri) > 1:
                return -1

            return max(le, ri) + 1
        

        return dfs(root) != -1