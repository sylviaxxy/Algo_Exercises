# 98. Validate Binary Search Tree
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution_wrong:
    # first attempt, a wrong solution
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        elif (root.left is None) and (root.right is None):
            return True
        else:
            if (root.left.val > root.val) or (root.right.val < root.val):
                return False
            else:
                return self.isValidBST(root.left) and self.isValidBST(root.right) 
      
class Solution_1:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            
            if not helper(node.left, lower, node.val):
                return False
            
            if not helper(node.right, node.val, upper):
                return False          
            
            return True
        
        return helper(root)