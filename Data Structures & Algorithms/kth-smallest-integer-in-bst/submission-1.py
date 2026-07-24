# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # lst = []

        # def dfs(node):
        #     nonlocal lst

        #     if not node:
        #         return 
        #     lst.append(node.val) #core function inside our DFS

        #     dfs(node.left)
        #     dfs(node.right)

        # dfs(root)
        # lst.sort()

        # return lst[k - 1]

        
        
        lst = []

        def inorder_dfs(node):
            if not node:
                return
            nonlocal lst

            inorder_dfs(node.left)
            lst.append(node.val)
            inorder_dfs(node.right)
        
        inorder_dfs(root)

        return lst[k - 1]
