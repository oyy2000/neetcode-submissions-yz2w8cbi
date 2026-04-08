# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #BFS
        q = deque([root])
        seq = []
        while q:
            
            # for i in range(len(q)):
                node = q.popleft()
                if node == None:
                    seq.append("null")
                    continue
                else:
                    seq.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
        return str(seq)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = ast.literal_eval(data)
        if not arr:
            return None
        if arr[0] == "null":
            return None
        root = TreeNode(arr[0])
        q = deque([root])
        i = 1
        n = len(arr)
        while q and i < n:
            node = q.popleft()

            if i < n and arr[i] != "null":
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i+=1
            if i < n and arr[i] != "null":
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i+=1

        return root

        
