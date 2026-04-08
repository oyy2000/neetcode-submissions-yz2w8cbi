# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root): 
        if root == None:
            return 
        self.helper(root.left)
        
        self.helper(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return 
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        print(root)
        self.helper(root)
        return root