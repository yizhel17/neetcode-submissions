# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        
        # ans = []
        # que = collections.deque([root])

        # while que:
        #     cur = []
        #     size = len(que)
        #     for _ in range(size):
        #         node = que.popleft()
        #         cur.append(node.val)

        #         if node.left:
        #             que.append(node.left)
        #         if node.right:
        #             que.append(node.right)
                
        #     ans.append(cur)
        
        # return ans

        
        #DFS的方法, 每一层的共同点就是深度相同,因此我们用hashmap来表示

        my_map = collections.defaultdict(list)
        
        def dfs(node, depth):
            if not node:
                return
        
            my_map[depth].append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)

        return (list(my_map.values()))