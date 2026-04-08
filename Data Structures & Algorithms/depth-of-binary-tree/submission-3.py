# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_d = 0
    count = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.max_d

    def helper(self, root):
        if root == None:
            return 
        self.count += 1
        self.helper(root.left)
        self.helper(root.right)
        self.max_d = max(self.max_d, self.count)
        self.count -= 1