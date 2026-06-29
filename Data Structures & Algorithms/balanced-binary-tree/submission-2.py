class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # dfs 规定返回格式：(is_balanced: bool, height: int)
        def dfs(node):
            if not node:
                # 拨乱反正：空节点绝对平衡，高度为 0
                return (True, 0)
            
            # 1. 探测左子树，直接解包拿到两个数据
            left_balanced, left_height = dfs(node.left)
            # 如果左边已经烂了，直接向上传递 False。高度多少已经无所谓了，填个 0 敷衍一下
            if not left_balanced:
                return (False, 0)
            
            # 2. 探测右子树
            right_balanced, right_height = dfs(node.right)
            # 如果右边烂了，同样拉响警报
            if not right_balanced:
                return (False, 0)

            # 3. 核心计算：因为 left_height 和 right_height 确定是纯数字了，可以安全相减
            if abs(left_height - right_height) > 1:
                return (False, 0)

            # 4. 一切安全，返回 True，并上报自己的真实高度
            return (True, max(left_height, right_height) + 1)
        
        # 终极清算：直接提取解包后的第一个布尔值
        is_balanced, height = dfs(root)
        return is_balanced