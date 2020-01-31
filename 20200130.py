class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
        
def print_all(node):
    if node is None:
        return
    print(node.val)
    print_all(node.left)
    print_all(node.right)
  
def count(node):
    """
    :return:
        Number of nodes in tree rooted at `node`.
    """
    if node is None:
        return 0
    print(f"I am at {node.val}")
    return 1+count(node.left)+count(node.right)
   
    
    
def check_balanced(node):
    """
    :return:
        height if all balanced, or None if the tree is not balanced
    """
    if node is None:
        return 0
        
    left_height = check_balanced(node.left)
    if left_height is None:
        return None
        
    # At this point left_height is an integer
    
    right_height = check_balanced(node.right)
    if right_height is None:
        return None
    
    # At this point...
    
    height = 1 + max(left_height, right_height)

    return height # "I am balanced, and my height is ..."
    
    
    
def identical(root1, root2) -> bool:
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    # Now root1 is not None, and root2 is not None:
    return (
        root1.val == root2.val and
        identical(root1.left, root2.left) and
        identical(root1.right, root2.right)
    )
    
    
     
def symmetric(root1, root2) -> bool:
    """
    Whether two trees `root1` and `root2` mirror each other.
    """
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    # Now root1 is not None, and root2 is not None:
    return (
        root1.val == root2.val and
        symmetric(root1.left, root2.right) and
        symmetric(root1.right, root2.left)
    )

def tree_symmetric(node) -> bool: 
    return symmetric(node.left, node.right)


def has(root, val) -> bool:
    if root is None:
        return None
    elif root.val == val:
        return True
    elif val < root.val:
        return has(root.left, val)
    else:
        return has(root.right, val)
        
        
        
def print_range(node, start, end):
    """
    start, end inclusive;
    assumption: node values are distinct.
    """
    if node is None:
        return
        
    if start < node.val:
        print_range(node.left, start, end)
    
    if start <= node.val <= end:
        print(node.val)
        
    if node.val < end:
        print_range(node.right, start, end)


 