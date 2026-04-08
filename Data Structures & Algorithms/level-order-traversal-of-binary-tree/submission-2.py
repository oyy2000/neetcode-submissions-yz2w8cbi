from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        stack = [(root, 0)]  # 栈中存放 (node, depth)

        while stack:
            node, depth = stack.pop()

            # 如果是新的一层，先扩容 res
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)

            # 注意：因为是栈 (LIFO)，要先压右再压左
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

        return res
