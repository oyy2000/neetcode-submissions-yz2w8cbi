# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         如果节点为空，直接返回。
# 交换当前节点的左右子树。
# 递归翻转左子树。
# 递归翻转右子树。
# 返回根节点。
        if root == None:
            return

        root.left, root.right = root.right, root.left 
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
        