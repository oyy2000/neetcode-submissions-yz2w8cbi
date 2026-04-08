from collections import deque
import json

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root):
        """输出 JSON 字符串，如 [1,2,3,null,null,4,5]"""
        if not root:
            return "[]"
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if node is None:
                res.append(None)          # JSON 里会变成 null
            else:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
        # 裁掉尾部多余的 null
        while res and res[-1] is None:
            res.pop()
        return json.dumps(res)

    def deserialize(self, data):
        """从 JSON 字符串恢复树，兼容稀疏层序（含 null 空洞）"""
        if not data or data == "[]":
            return None

        # 解析 JSON；若上游传来单引号或 'None'，做个宽松修复
        try:
            vals = json.loads(data)
        except json.JSONDecodeError:
            data_norm = data.replace("'", '"').replace("None", "null")
            vals = json.loads(data_norm)

        if not vals or vals[0] is None:
            return None

        root = TreeNode(vals[0])
        q = deque([root])
        i = 1
        n = len(vals)

        # 队列法连接左右孩子：能够正确处理 [1,null,3,4,5,6,7] 这类不规则层序
        while q and i < n:
            node = q.popleft()

            if i < n and vals[i] is not None:
                node.left = TreeNode(vals[i])
                q.append(node.left)
            i += 1

            if i < n and vals[i] is not None:
                node.right = TreeNode(vals[i])
                q.append(node.right)
            i += 1

        return root
