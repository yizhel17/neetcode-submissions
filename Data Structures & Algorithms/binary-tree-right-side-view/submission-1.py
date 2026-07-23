# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []

        que = collections.deque([root])

        while que:
            q_size = len(que)
            cur = []
            
            for _ in range(q_size):
                node = que.popleft()
                cur.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            ans.append(cur[-1])

            
        return ans
