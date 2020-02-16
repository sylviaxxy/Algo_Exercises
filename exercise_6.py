#LC 701. Insert into a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        #It is guaranteed that the new value does not exist in the original BST.
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root