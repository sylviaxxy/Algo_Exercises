# Count BST nodes that lie in a given range
# Given a Binary Search Tree (BST) and a range, count number of nodes that lie in the given range.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countBSTRange(self, root, lower, upper):
        if not root:
            return 0
        
        if lower < root.val < upper:
            return (1 + self.countBSTRange(root.left, lower, root.val) 
                + self.countBSTRange(root.right, root.val, upper))

        if upper < root.val:
            return self.countBSTRange(root.left, lower, upper)

        if lower > root.val: 
            return self.countBSTRange(root.right, lower, upper)