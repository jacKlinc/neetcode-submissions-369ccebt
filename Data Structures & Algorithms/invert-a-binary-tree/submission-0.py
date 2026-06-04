# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # https://youtu.be/EPwWrs8OtfI
        # The lower levels are called "subtrees"
        # All lowers nodes are called "leaf nodes"
        # [1,2,3,4,5,6,7] is an example of a "perfect tree" where all levels are filled
        # The tree on the left has a height or depth of 3

        # DFS: Depth-First Search. Go down the tree: 
            # 1 -> 2 -> 4, 2 -> 5, 1 -> 3 -> 6, 3 -> 7
        # Imeplemented using a Stack using recursion

        # Preorder: look at .val first, .left, .right
        # Inorder: look at .left first, .val, .right
        # Postorder: look at .left first, .right, .val


        # BFS: Breadth-First Search AKA Level-order traversal. Go across the tree: 
            # 1 -> 2 -> 3, 4 -> 5 -> 6 -> 7

        # Imeplemented using a Queue
        if not root:
            return None
        
        left = root.left
        root.left = root.right
        root.right = left
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root